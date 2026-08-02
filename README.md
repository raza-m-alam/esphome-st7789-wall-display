# ESPHome ST7789 Wall Display

A reusable local-first ESPHome starter for an ESP32-S3 and a portrait
170x320 ST7789V display. It supports:

- Embedded still images
- Embedded GIF animation
- Alternating still/animation mode
- Runtime JPEG loading from Home Assistant or another HTTP server
- Home Assistant mode selection, refresh, backlight, restart, and status
- Wi-Fi fallback and delayed BLE setup recovery
- A media preparation tool for images, GIFs, MP4s, and MOVs

## Tested hardware profile

This repository begins with one empirically tested profile:

| Function | Setting |
|---|---|
| ESP32 board | `esp32-s3-devkitc-1` |
| Flash | 16 MB |
| Framework | ESP-IDF |
| PSRAM | Octal, 80 MHz |
| Display | ST7789V, 170x320 portrait |
| SPI clock | GPIO12 |
| SPI MOSI | GPIO11 |
| CS | GPIO10 |
| DC | GPIO9 |
| Reset | GPIO13 |
| Backlight | GPIO14 |
| Width offset | 35 |
| Color order | BGR |
| Driver inversion | Off |
| Color depth | 16-bit |
| SPI rate | 10 MHz |

Other ST7789 boards may require different pins, offsets, color order, or
inversion. Do not assume this is a universal ST7789 profile.

## Quick start

1. Copy the repository into the ESPHome configuration directory.
2. Merge the names from `secrets.example.yaml` into ESPHome's active
   `secrets.yaml`.
3. Replace every placeholder with a real value.
4. Validate and compile `wall-display.yaml`.
5. Install only after preserving the last known-good firmware and YAML.

## Use your own image

Install the Python dependency:

```powershell
py -m pip install -r .\requirements.txt
```

Prepare a normal photograph:

```powershell
py .\tools\prepare_media.py .\my-photo.jpg
```

The default output is:

```text
assets/user/background_panel.png
```

Change this substitution in `wall-display.yaml`:

```yaml
compiled_image_file: "assets/user/background_panel.png"
```

Recompile and install the firmware.

## Use a GIF, MP4, or MOV

Video conversion requires FFmpeg on `PATH`.

```powershell
py .\tools\prepare_media.py .\my-video.mp4
```

The default output is:

```text
assets/user/animation_panel.gif
```

Change this substitution:

```yaml
compiled_animation_file: "assets/user/animation_panel.gif"
```

Recompile and install.

ESPHome does not directly play MP4 or MOV files in this configuration.
The tool extracts and prepares frames, then creates an embedded GIF.

## Runtime JPEG

Place a baseline JPEG in Home Assistant's `/config/www/wall_display/`
directory and serve it at:

```text
http://homeassistant.local:8123/local/wall_display/current.jpg
```

You can also enter another URL through the `Remote JPEG URL` entity and
press `Refresh Remote JPEG`.

Runtime JPEG color is still a physical validation item for the tested
panel. Compiled PNG/GIF compensation is proven; do not claim equivalent
runtime color until the calibration test passes.

## Privacy

Never commit:

- `secrets.yaml`
- Family photographs or videos
- Household names
- Wi-Fi names or passwords
- API or OTA credentials
- Private IP addresses or MAC addresses
- Home Assistant entity IDs tied to a private home
- Raw logs containing network or device details

`assets/user/` is ignored by Git for this reason.

## Status

This is a **first-commit candidate**, not a public release. The required
physical validation is documented in `docs/validation.md`.
