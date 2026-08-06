# ESPHome ST7789 Wall Display

A local-first ESPHome starter for portrait 170x320 ST7789V wall displays.
It supports a physically validated ESP32-S3 profile, a reduced-memory classic
ESP32 profile, Home Assistant controls, OTA updates, local remote-JPEG loading,
and guarded BLE provisioning.

## Release profiles

| Configuration | Status |
|---|---|
| `install/st7789-wall-display-s3.yaml` | Primary ESP32-S3 installation profile; physically validated |
| `wall-display-esp32-classic-test.yaml` | Advanced classic ESP32 profile; physically validated |
| `wall-display.yaml` | Full compiled-media development profile; not the primary installation path |

## Primary ESP32-S3 profile

The primary release candidate was tested on an ESP32-S3 N16R8 module.

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

Physically verified behavior:

- correct RGBW geometry and color output;
- eight-frame animation and timed demo rotation;
- immediate display-mode changes;
- encrypted Native API connectivity;
- device-specific OTA password and successful wireless updates;
- local JPEG download with explicit `Downloading`, `Loaded`, and `Error` states;
- BLE Start turns the backlight off before enabling BLE;
- BLE Stop disables BLE and restores the prior display state;
- no visible BLE flicker while the protected backlight behavior is active.

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

The reduced classic framebuffer is intentional. A full 108,800-byte buffer
caused severe resource pressure when Wi-Fi and BLE were enabled together on a
non-PSRAM ESP32. The 13,600-byte profile remained stable during physical
Wi-Fi, API, display, and BLE testing.

## Install the S3 profile

1. Download `install/st7789-wall-display-s3.yaml`.
2. In Home Assistant, open **ESPHome Device Builder**.
3. Select **Create device** and then **Import from File**.
4. Open the imported configuration in Device Navigator.
5. Add the user's local Wi-Fi SSID and password.
6. Enable Native API encryption and let Device Builder generate a unique key.
7. Add a unique ESPHome OTA password.
8. Validate the configuration.
9. Perform the first installation over USB.
10. Use OTA for later updates.

The imported configuration uses a fixed hostname and does not append a MAC
suffix. Device Builder can therefore track the same hostname that the device
announces after installation.

## Device-specific credentials

The installation file contains no real SSID, Wi-Fi password, API encryption
key, OTA password, private address, or `!secret` reference. Device Builder
creates the user's local secret references when the device is configured.

Recommended credential behavior:

- Wi-Fi values remain local to the user's ESPHome installation;
- each device receives its own API encryption key;
- each device receives its own OTA password;
- generated secret values are never committed to this repository.

## Remote JPEG

The S3 profile can load a baseline JPEG from Home Assistant or another local
HTTP server.

A typical Home Assistant location is:

```text
/config/www/wall_display/current.jpg
```

Home Assistant serves that file at:

```text
http://homeassistant.local:8123/local/wall_display/current.jpg
```

The exact URL is editable through the `Remote JPEG URL` entity. Press
`Refresh Remote JPEG` after changing the URL. The diagnostic status reports
`Downloading`, `Loaded`, or `Error`; the display shows an orange loading frame
or red error frame rather than silently displaying a stale placeholder.

## BLE provisioning behavior

BLE is disabled during normal operation.

1. Normal Wi-Fi is attempted first.
2. BLE provisioning can be started manually or after the recovery delay.
3. The TFT backlight is forced off before BLE starts.
4. The Backlight control refuses to turn the panel on while BLE is active.
5. BLE ends when the user presses `Stop BLE Setup`, Wi-Fi reconnects, or the
   10-minute setup window expires.
6. The prior backlight state and display mode are restored afterward.

This behavior was added because active BLE caused visible backlight flicker on
both tested boards when the panel remained illuminated. The image data stayed
intact; keeping the panel dark removes the visible artifact.

## Deterministic classic test image

The classic profile includes a deterministic vector test card:

```text
assets/demo/display_test_card.svg
```

Its exact-byte SHA-256 fingerprint is stored beside it:

```text
assets/demo/display_test_card.svg.sha256
```

The file contains no embedded personal information, C2PA metadata, SynthID,
or other generative-image provenance marker.

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

GitHub Actions validates and compiles the primary S3 installation profile, the
classic ESP32 profile, and the full-media development profile using ESPHome.
Physical results and release gates are recorded in `PRECOMMIT_CHECKLIST.md`.

## Project status

The repository remains private while the release history is cleaned and the
license decision is recorded. Hardware validation is complete for the primary
S3 installation profile and the advanced classic ESP32 profile. No release or
visibility change occurs without explicit approval.
