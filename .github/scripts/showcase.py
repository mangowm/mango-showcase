import datetime
import os
import re
import sys
from urllib.parse import urlparse

import yaml


class InlineList(list):
    pass


class Dumper(yaml.SafeDumper):
    pass


Dumper.add_representer(
    InlineList,
    lambda dumper, data: dumper.represent_sequence(
        "tag:yaml.org,2002:seq", data, flow_style=True
    ),
)


def load():
    with open("entries.yml", encoding="utf-8") as f:
        return yaml.safe_load(f) or []


def save(entries):
    for entry in entries:
        entry["tags"] = InlineList(entry.get("tags") or [])
    with open("entries.yml", "w", encoding="utf-8") as f:
        yaml.dump(
            entries,
            f,
            Dumper=Dumper,
            default_flow_style=False,
            allow_unicode=True,
            sort_keys=False,
        )


def output(**values):
    with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as f:
        for key, value in values.items():
            print(f"{key}={value}", file=f)


def field(body, label):
    match = re.search(rf"### {label}\s*\n+(.+)", body)
    value = match.group(1).strip() if match else ""
    return "" if value == "_No response_" else value


command = sys.argv[1] if len(sys.argv) > 1 else ""

if command == "add":
    body = os.environ["ISSUE_BODY"]
    username = os.environ["ISSUE_AUTHOR"]
    dotfiles = field(body, "Dotfiles URL")
    tags = [
        tag.strip().lower()
        for tag in field(body, "Tags").split(",")
        if tag.strip()
    ]

    url = urlparse(dotfiles)
    repo = url.path.strip("/")
    if (
        url.scheme != "https"
        or url.hostname != "github.com"
        or repo.count("/") != 1
        or repo.lower().endswith(".git")
    ):
        output(valid="false", reason="invalid_url")
        sys.exit(0)

    dotfiles = f"https://github.com/{repo}"

    entries = load()
    if any(e.get("username", "").lower() == username.lower() for e in entries):
        output(valid="false", reason="duplicate_username")
        sys.exit(0)
    if any(e.get("dotfiles", "").rstrip("/") == dotfiles for e in entries):
        output(valid="false", reason="duplicate_url")
        sys.exit(0)

    entries.append({"username": username, "dotfiles": dotfiles, "tags": tags})
    save(entries)
    output(valid="true", username=username, repo=repo)

elif command == "timestamps":
    entries = load()
    now = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
    users = []
    for entry in entries:
        if "added" not in entry:
            entry["added"] = now
            users.append(entry["username"])

    if users:
        save(entries)
        print(f"Added timestamps to {len(users)} entr{'y' if len(users) == 1 else 'ies'}")
        output(changed="true", usernames=", ".join(f"@{user}" for user in users))
    else:
        print("No entries need timestamps.")

else:
    sys.exit("usage: showcase.py {add|timestamps}")
