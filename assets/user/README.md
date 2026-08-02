# Local user media

This directory is intentionally ignored by Git except for this README and
`.gitkeep`.

Generate panel-ready media here:

```powershell
py .\tools\prepare_media.py .\my-photo.jpg
py .\tools\prepare_media.py .\my-video.mp4
```

Then change only these substitutions in `wall-display.yaml`:

```yaml
compiled_image_file: "assets/user/background_panel.png"
compiled_animation_file: "assets/user/animation_panel.gif"
```

Never commit family photographs, private videos, household names, or other
personal media to a public repository.
