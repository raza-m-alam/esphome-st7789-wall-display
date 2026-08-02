# Media workflow

## Compiled media

Compiled PNG and GIF assets are transformed into firmware during the
ESPHome build. Changing either requires a recompile and firmware upload.

The tested panel's proven pipeline is:

1. Resize/crop each frame to 170x320.
2. Fully invert all RGB channels.
3. Save PNG or animated GIF.
4. Load in ESPHome as `type: RGB`.
5. Keep the display driver at BGR, inversion off, 16-bit color.

The compensated file will look like a photographic negative on a normal
monitor. It should look natural on the tested panel.

## Runtime media

Runtime media is downloaded over HTTP and does not require recompiling when
only the JPEG changes. Direct SMB browsing and direct MP4/MOV playback are
not part of this design.

The runtime JPEG path remains experimental until red/green/blue/white
calibration is physically verified.

## Converter examples

Fill the screen by cropping:

```powershell
py .\tools\prepare_media.py .\photo.jpg --fit crop
```

Preserve the entire source with letterboxing:

```powershell
py .\tools\prepare_media.py .\photo.jpg --fit contain
```

Convert up to eight seconds of video at eight frames per second:

```powershell
py .\tools\prepare_media.py .\clip.mp4 --fps 8 --max-seconds 8
```

Prepare media for a different panel that does not require source inversion:

```powershell
py .\tools\prepare_media.py .\photo.jpg --no-invert
```
