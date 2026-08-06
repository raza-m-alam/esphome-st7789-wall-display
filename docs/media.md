# Media workflow

The repository has two separate media paths. Use the primary S3 installation
profile for normal installation. Use the compiled-media development profile
only when embedding custom PNG, GIF, or converted video assets into firmware.

## Primary S3 profile: runtime JPEG

`install/st7789-wall-display-s3.yaml` loads a baseline JPEG over HTTP. Changing
the file or URL does not require recompiling firmware.

A typical Home Assistant file path is:

```text
/config/www/wall_display/current.jpg
```

Home Assistant serves it at:

```text
http://homeassistant.local:8123/local/wall_display/current.jpg
```

Set that URL through `Remote JPEG URL`, then press `Refresh Remote JPEG`.
`Remote JPEG Status` reports `Downloading`, `Loaded`, or `Error`.

Requirements:

- the source must be a valid baseline JPEG;
- the ESPHome device must be able to reach the HTTP server;
- the URL path must match the file below `/config/www/` exactly;
- a numeric Home Assistant address can be used when `.local` name resolution
  is unavailable.

Runtime JPEG geometry and color were physically validated on the documented S3
profile.

## Compiled-media development profile

`wall-display.yaml` embeds media into firmware. Changing embedded media requires
a new compile and firmware upload.

The development profile's tested source-compensation pipeline is:

1. Resize or crop each frame to 170x320.
2. Apply the profile's RGB compensation.
3. Save a PNG or animated GIF.
4. Load it in ESPHome as `type: RGB`.
5. Compile and install the updated firmware.

The compensated source can look like a photographic negative on a normal
monitor. That is expected for this development profile.

## Converter examples

Install dependencies:

```powershell
py -m pip install -r .\requirements.txt
```

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

Prepare media for a panel that does not require the development profile's
source inversion:

```powershell
py .\tools\prepare_media.py .\photo.jpg --no-invert
```

Video conversion requires a user-installed FFmpeg executable on `PATH`. FFmpeg
is not bundled with this repository.
