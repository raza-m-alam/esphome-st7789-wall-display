# ESPHome ST7789 Wall Display

A local-first wall-display starter for portrait 170x320 ST7789V panels. The
repository includes a primary ESP32-S3 installation profile, a reduced-memory
classic ESP32 profile, Home Assistant controls, local JPEG loading, animation,
and a separate compiled-media development profile.

## Profiles

| Configuration | Version | Status |
|---|---:|---|
| `install/st7789-wall-display-s3.yaml` | `0.1.0` | Primary ESP32-S3 profile; physically validated |
| `wall-display-esp32-classic.yaml` | `0.1.0` | Advanced classic ESP32 profile; physically validated |
| `wall-display.yaml` | `0.2.0-dev` | Compiled-media development profile |

The project remains pre-1.0, so filenames and configuration details may evolve
before a future compatibility commitment.

## Primary ESP32-S3 profile

The primary profile was tested on an ESP32-S3 N16R8 module.

| Function | Setting |
|---|---|
| Board | `esp32-s3-devkitc-1` |
| Flash | 16 MB |
| PSRAM | 8 MB octal, 80 MHz |
| Framework | ESP-IDF |
| Display | ST7789V, 170x320 portrait |
| SPI clock / MOSI | GPIO12 / GPIO11 |
| CS / DC / reset | GPIO10 / GPIO9 / GPIO13 |
| Backlight | GPIO14 |
| Width offset | 35 |
| Color order / inversion | BGR / on |
| Buffer | 100% / 108,800 bytes in PSRAM |
| SPI rate | 10 MHz |

Verified behavior includes RGBW output, an eight-frame animation, timed demo
rotation, Home Assistant controls, encrypted Native API, password-protected
OTA, local JPEG loading, and BLE setup with the display backlight suppressed.

## Install the S3 profile

> **Security:** This credential-free file is intended for ESPHome Device
> Builder import. Do not compile or flash it directly until API encryption and
> an OTA password have been configured.

1. Download `install/st7789-wall-display-s3.yaml`.
2. In Home Assistant, open **ESPHome Device Builder**.
3. Select **Create device**, then **Import from File**.
4. Add the Wi-Fi SSID and password in Device Navigator.
5. Enable Native API encryption and generate a unique key.
6. Add a unique ESPHome OTA password.
7. Validate the configuration.
8. Perform the first installation over USB.
9. Use OTA for later updates.

The profile uses a fixed hostname so Device Builder tracks the same name the
device announces after installation. Before importing a second display, change
the `name` substitution so the two devices do not collide on the network.

## Remote JPEG

The S3 profile can load a baseline JPEG at runtime. A typical Home Assistant
file and URL are:

```text
/config/www/wall_display/current.jpg
http://homeassistant.local:8123/local/wall_display/current.jpg
```

Set the URL through `Remote JPEG URL`, then press `Refresh Remote JPEG`.
`Remote JPEG Status` reports `Downloading`, `Loaded`, or `Error`.

The default URL uses local HTTP. Keep the image endpoint on a trusted LAN and
do not expose it directly to the internet.

## BLE setup and recovery

BLE is disabled during normal operation. It can be enabled manually or after a
Wi-Fi recovery delay, and the setup window closes after 10 minutes or when
Wi-Fi reconnects.

The tested hardware has no dedicated authorization button, so ESPHome Improv
uses `authorizer: none`. Anyone within BLE range during an active setup window
could submit Wi-Fi credentials. The time limit reduces exposure, but it is not
a user-authentication control.

On the primary S3 profile, the backlight is forced off before BLE starts and
cannot be turned back on until BLE stops. This protects the display from the
visible flicker observed during testing; it does not authorize the person
performing provisioning.

## Classic ESP32 profile

| Function | Setting |
|---|---|
| Board | `esp32dev` / ESP32-WROOM-32D |
| Framework | ESP-IDF |
| Display | ST7789V, 170x320 portrait |
| SPI clock / MOSI | GPIO18 / GPIO23 |
| CS / DC / reset | GPIO22 / GPIO16 / GPIO17 |
| Backlight | GPIO4 |
| Width offset | 35 |
| Color order / inversion | BGR / on |
| Buffer | 12.5% / 13,600 bytes |
| SPI rate | 5 MHz |

A full framebuffer created severe resource pressure when Wi-Fi and BLE were
enabled together on the non-PSRAM board. The reduced buffer remained stable in
physical testing. Its drawing lambda has no side effects because ESPHome calls
that lambda once per buffer segment.

The classic profile uses the simpler tested mitigation of turning the
backlight off while BLE is active. Do not turn the exposed Backlight entity
back on during that window, or the visible flicker may return.

## Compiled-media development profile

`wall-display.yaml` is intentionally ahead of the release profiles at
`0.2.0-dev`. It embeds PNG/GIF media into firmware and retains the tested source
color-compensation pipeline. It is not the normal installation path and does
not include the primary S3 profile's full BLE backlight guard.

See `docs/media.md` and `tools/prepare_media.py` for the media workflow.

## Testing

- GitHub Actions validates and compiles all three ESPHome profiles.
- Python utility tests and linting run in a separate CI job.
- Physical test details are recorded in `TESTING.md` and
  `docs/validation.md`.

## Local files

`assets/user/`, local overrides, credentials, and raw diagnostic exports are
ignored by Git. Keep personal media and device-specific configuration local.
The SHA-256 sidecar for the public SVG test card is retained as an integrity
fingerprint for that deterministic asset.

## License

Original content is available under the MIT License. ESPHome and other upstream
components retain their own licenses; see `THIRD_PARTY_NOTICES.md` before
redistributing compiled firmware.
