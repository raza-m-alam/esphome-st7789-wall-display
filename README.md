# ESPHome ST7789 Wall Display

A reusable, local-first ESPHome starter for portrait 170x320 ST7789V
wall displays.

## Current profiles

| Configuration | Status |
|---|---|
| `wall-display.yaml` | Full ESP32-S3 media starter |
| `wall-display-esp32-classic-test.yaml` | Classic ESP32 hardware and BLE-recovery validation |

The classic ESP32 profile has verified display geometry, RGB output, Wi-Fi,
and reduced-memory buffering. Full PNG/GIF/JPEG behavior on that profile is
still a physical validation item and is not presented as complete.

## ESP32-S3 hardware profile

| Function | Setting |
|---|---|
| Board | `esp32-s3-devkitc-1` |
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
| Buffer | 100% in PSRAM |
| SPI rate | 10 MHz |

## Classic ESP32 test profile

| Function | Setting |
|---|---|
| Board | `esp32dev` / ESP32-WROOM-32D |
| Framework | ESP-IDF |
| Display | ST7789V, 170x320 portrait |
| SPI clock | GPIO18 |
| SPI MOSI | GPIO23 |
| CS | GPIO22 |
| DC | GPIO16 |
| Reset | GPIO17 |
| Backlight | GPIO4 |
| Width offset | 35 |
| Color order | BGR |
| Driver inversion | On |
| Buffer | 12.5% / 13,600 bytes |
| SPI rate | 5 MHz |

Other boards may require different pins, offsets, color order, inversion, or
buffering. Do not assume either profile is universal.

## Secrets

The repository uses generalized ESPHome secret names:

```yaml
wifi_ssid: "..."
wifi_password: "..."
fallback_ap_password: "..."
ota_password: "..."
api_encryption_key: "..."
```

Copy `secrets.example.yaml` into ESPHome's active `secrets.yaml`, or generate
random API, OTA, and fallback-AP values locally:

```powershell
py .\tools\generate_secrets.py
```

The generated file is ignored by Git. Replace its Wi-Fi placeholders and
merge the values into the active ESPHome `secrets.yaml`.

## Quick start

1. Copy the repository into the ESPHome configuration directory.
2. Add the generalized secret keys to ESPHome's active `secrets.yaml`.
3. Choose the configuration that matches the physical board.
4. Validate and compile it.
5. Preserve the last known-good YAML and firmware before installation.
6. Perform the first installation over USB.

## Wi-Fi and BLE recovery

The configurations keep BLE disabled during normal operation:

1. Attempt normal Wi-Fi first.
2. If Wi-Fi remains unavailable for 90 seconds, enable BLE Improv.
3. Keep BLE provisioning available for up to 20 minutes.
4. Disable BLE immediately when Wi-Fi connects.
5. Start the fallback access point after the BLE window.

The classic profile deliberately uses a 12.5% display buffer. A full
108,800-byte framebuffer caused severe resource pressure when Wi-Fi and BLE
were enabled together on a non-PSRAM ESP32.

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

ESPHome does not directly play MP4 or MOV files in this configuration. The
preparation tool extracts frames and creates an embedded GIF.

## Runtime JPEG

Place a baseline JPEG in Home Assistant's `/config/www/wall_display/`
directory and serve it at:

```text
http://homeassistant.local:8123/local/wall_display/current.jpg
```

You can also enter another URL through the `Remote JPEG URL` entity and press
`Refresh Remote JPEG`.

Runtime JPEG color remains a physical validation item for the S3 profile.
Compiled PNG/GIF compensation is proven; equivalent runtime color should not
be claimed until calibration passes.

## Privacy and repository hygiene

Never commit:

- `secrets.yaml`
- Family photographs or videos
- Household or network names
- Wi-Fi, API, or OTA credentials
- Private IP addresses, MAC addresses, or BSSIDs
- Home Assistant entity IDs tied to a private home
- Raw ESPHome logs containing network or device details

`assets/user/`, local overrides, and common raw-log export names are ignored
by Git.

## Status

This repository remains private and under hardware validation. It is not a
public release.
