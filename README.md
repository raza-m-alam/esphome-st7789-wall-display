# ESPHome ST7789 Wall Display

A local-first ESPHome starter for portrait 170x320 ST7789V wall displays.
It provides a primary ESP32-S3 installation profile, an advanced reduced-memory
classic ESP32 profile, Home Assistant controls, OTA updates, local JPEG
loading, animation, and guarded BLE provisioning.

## Release profiles

| Configuration | Status |
|---|---|
| `install/st7789-wall-display-s3.yaml` | Primary ESP32-S3 profile; physically validated |
| `wall-display-esp32-classic.yaml` | Advanced classic ESP32 profile; physically validated |
| `wall-display.yaml` | Compiled-media development profile; not the primary installation path |

The first public release is `0.1.0`. The supported installation surface may
still evolve before a future `1.0.0` stability commitment.

## Primary ESP32-S3 profile

The primary profile was tested on an ESP32-S3 N16R8 module.

| Function | Setting |
|---|---|
| Board | `esp32-s3-devkitc-1` |
| Flash | 16 MB |
| PSRAM | 8 MB octal, 80 MHz |
| Framework | ESP-IDF |
| Display | ST7789V, 170x320 portrait |
| SPI clock | GPIO12 |
| SPI MOSI | GPIO11 |
| CS | GPIO10 |
| DC | GPIO9 |
| Reset | GPIO13 |
| Backlight | GPIO14 |
| Width offset | 35 |
| Color order | BGR |
| Driver inversion | On |
| Buffer | 100% / 108,800 bytes in PSRAM |
| SPI rate | 10 MHz |

Verified behavior:

- correct RGBW geometry and color output;
- eight-frame animation and timed demo rotation;
- immediate display-mode changes;
- encrypted Native API connectivity;
- device-specific OTA password and successful wireless updates;
- local JPEG download with explicit `Downloading`, `Loaded`, and `Error` states;
- BLE Start turns the backlight off before enabling BLE;
- BLE Stop disables BLE and restores the prior display state;
- no visible BLE flicker while the protected backlight behavior is active.

## Install the S3 profile

1. Download `install/st7789-wall-display-s3.yaml`.
2. In Home Assistant, open **ESPHome Device Builder**.
3. Select **Create device**, then **Import from File**.
4. Open the imported configuration in Device Navigator.
5. Add the local Wi-Fi SSID and password.
6. Enable Native API encryption and let Device Builder generate a unique key.
7. Add a unique ESPHome OTA password.
8. Validate the configuration.
9. Perform the first installation over USB.
10. Use OTA for later updates.

The imported configuration uses a fixed hostname and does not append a MAC
suffix. Device Builder therefore tracks the same hostname that the device
announces after installation.

## Device-specific credentials

The primary installation file contains no real SSID, Wi-Fi password, API key,
OTA password, private address, or `!secret` reference. Device Builder creates
local secret references when the user configures the device.

Recommended behavior:

- Wi-Fi values remain in the user's ESPHome installation;
- each device receives its own API encryption key;
- each device receives its own OTA password;
- generated secret values are never committed to this repository.

## Remote JPEG

The S3 profile can load a baseline JPEG from Home Assistant or another local
HTTP server. A typical Home Assistant location is:

```text
/config/www/wall_display/current.jpg
```

Home Assistant serves that file at:

```text
http://homeassistant.local:8123/local/wall_display/current.jpg
```

The exact URL is editable through the `Remote JPEG URL` entity. Press
`Refresh Remote JPEG` after changing it. The status reports `Downloading`,
`Loaded`, or `Error`, and the display uses a visible loading or error frame
instead of silently showing stale content.

## BLE provisioning behavior

BLE is disabled during normal operation.

1. Normal Wi-Fi is attempted first.
2. BLE provisioning can be started manually or after the recovery delay.
3. The TFT backlight is forced off before BLE starts.
4. The Backlight control refuses to illuminate the panel while BLE is active.
5. BLE ends when the user presses `Stop BLE Setup`, Wi-Fi reconnects, or the
   10-minute setup window expires.
6. The prior backlight state and display mode are restored afterward.

This behavior is intentional. Active BLE caused visible backlight flicker on
both tested boards when the panel remained illuminated. Display data remained
intact; keeping the panel dark removes the visible artifact.

## Classic ESP32 profile

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

The reduced framebuffer is deliberate. A full 108,800-byte buffer created
severe resource pressure when Wi-Fi and BLE were enabled together on a
non-PSRAM ESP32. The 13,600-byte profile remained stable during physical
Wi-Fi, API, display, and BLE testing.

The classic configuration is an advanced source profile. Copy the generalized
keys from `secrets.example.yaml` into the user's local ESPHome secrets file,
then validate and perform the first installation over USB.

## Compiled-media development profile

`wall-display.yaml` retains the embedded PNG/GIF and optional video-conversion
workflow used during development. It is kept separate from the primary
installation file so first-time users do not need local media assets or Python
tools merely to install the wall display.

See `docs/media.md` for the media pipeline and `tools/prepare_media.py` for
optional conversion of still images, GIFs, MP4s, and MOVs.

## Demo assets

The public demo PNG, GIF, and SVG files are project-specific test graphics.
They contain no personal photographs, household information, creator fields,
device identifiers, or location metadata. The exact bytes of the classic SVG
test card are recorded in `assets/demo/display_test_card.svg.sha256`.

## Privacy and repository hygiene

Never commit:

- `secrets.yaml`;
- Wi-Fi, API, or OTA credentials;
- private IP addresses, MAC addresses, or BSSIDs;
- household names or private Home Assistant entity IDs;
- family photographs or videos;
- raw ESPHome or installer logs.

`assets/user/`, local overrides, and common raw-log export names are ignored by
Git.

## Validation

GitHub Actions validates and compiles the primary S3 profile, the classic
ESP32 profile, and the full-media development profile. Physical results and
release gates are recorded in `PRECOMMIT_CHECKLIST.md` and
`docs/validation.md`.

## Authorship and project identifier

The intentional public project namespace is:

```text
razaalam.esphome_st7789_wall_display
```

It identifies this ESPHome project and is not a credential or household name.
Copyright ownership is recorded in `LICENSE` as **Raza M Alam**.

## License

Original content in this repository is available under the MIT License. See
`LICENSE`. Upstream tools and generated firmware components retain their own
licenses; see `THIRD_PARTY_NOTICES.md` before redistributing firmware binaries.

## Status

Hardware validation is complete for the primary S3 profile and advanced
classic ESP32 profile. The repository remains private until the release branch
is squash-merged, the final privacy check passes, and publication is explicitly
approved.
