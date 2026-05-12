import yaml

HEADER = """\
<div align="center">
  <img src="https://raw.githubusercontent.com/mangowm/mango/main/assets/mango-transparency-256.png" width="80"/>
  <h2>Mango Showcase</h2>
  <p>Community desktops powered by <a href="https://github.com/mangowm/mango">mangowm</a></p>
</div>

---

1. Fork this repo
2. Get a screenshot URL by dragging your image into any GitHub PR or issue description box
3. Add your entry to `entries.yml`:
   ```yaml
   - your-username:
       screenshot: https://github.com/user-attachments/assets/YOUR-IMAGE-ID
       dotfiles: https://github.com/your-username/dotfiles
   ```
4. Open a pull request

---

<div align="center">
<table>"""

FOOTER = """\
</table>
</div>"""

COLS = 2

with open("entries.yml") as f:
    raw = yaml.safe_load(f) or []

entries = []
for item in raw:
    username = next(iter(item))
    entries.append({"username": username, **item[username]})

rows = []
for i in range(0, len(entries), COLS):
    chunk = entries[i : i + COLS]
    cells = ""
    for entry in chunk:
        cells += (
            f"<td>\n\n"
            f'<img src="{entry["screenshot"]}" width="100%" height="250"/>\n\n'
            f'<p><a href="{entry["dotfiles"]}"><b>{entry["username"]}</b></a></p>\n\n'
            f"</td>\n"
        )
    rows.append(f'<tr align="center" valign="top">\n{cells}</tr>')

table = "\n".join(rows)

with open("README.md", "w") as f:
    f.write(f"{HEADER}\n{table}\n{FOOTER}\n")
