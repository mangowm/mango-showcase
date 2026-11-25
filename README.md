# <img src="https://raw.githubusercontent.com/mangowm/mango/main/assets/mango-transparency-256.png" width="28" height="28" alt="mango logo" style="vertical-align: middle;"> mango setup showcase

Live gallery: https://mangowm.github.io/showcase

## Add your setup

1. Add an entry to `entries.yml`. Your dotfiles repo must be public and hosted on GitHub.

```yaml
- username: <username>
  dotfiles: https://github.com/<username>/<repo>
  tags: [dark, minimal]
```

2. Add screenshots or videos to your dotfiles repo in a `showcase/` directory:

   | Type | Single file | Multiple files |
   |------|-------------|----------------|
   | **Screenshots** | `showcase/image.png` | `showcase/images/1.png`, `2.png`, ... |
   | **Videos** | `showcase/video.mp4` | `showcase/videos/1.mp4`, `2.mp4`, ... |

3. Open a pull request.

## Requirements

* Include `tags`, even if it is `[]`.
* Do **not** add `added`. The workflow adds it after merge.
