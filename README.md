# <img src="https://raw.githubusercontent.com/mangowm/mango/main/assets/mango-transparency-256.png" width="28" height="28" alt="Mango logo" style="vertical-align: middle;"> MANGO SETUP SHOWCASE

View the gallery: https://mangowm.github.io/showcase

## Add your setup

1. Edit `entries.yml` (your dotfiles repo must be public and hosted on **github** or **codeberg**):

```yaml
- username: your-username
  dotfiles: https://github.com/your-username/dotfiles
  tags: [dark, minimal]
```

2. Add assets to your dotfiles repo under a `showcase/` directory:

   | Type | Single file | Multiple files |
   |------|-------------|----------------|
   | **Screenshots** | `showcase/image.png` | `showcase/images/1.png`, `2.png`, ... |
   | **Videos** | `showcase/video.mp4` | `showcase/videos/1.mp4`, `2.mp4`, ... |

3. Open a pull request

## Requirements
* `tags` is required (can be `[]`).
* Do **not** add `added`. It is added automatically after merge.
