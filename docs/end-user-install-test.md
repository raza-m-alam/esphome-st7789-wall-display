# End-user installation verification

The primary ESP32-S3 manual-install profile is:

```text
install/st7789-wall-display-s3.yaml
```

## Verified user path

1. In Home Assistant, open **ESPHome Device Builder**.
2. Select **Create device** and then **Import from File**.
3. Import `st7789-wall-display-s3.yaml`.
4. In Device Navigator, add the user's Wi-Fi SSID and password.
5. Enable Native API encryption and let Device Builder generate a unique key.
6. Add a unique ESPHome OTA password.
7. Validate the configuration.
8. Perform the first installation over USB.
9. Use OTA for later updates.

The profile uses:

```yaml
name: "st7789-wall-display-s3"
name_add_mac_suffix: false
```

The fixed hostname prevents the manually imported Device Builder entry from
tracking a different MAC-suffixed hostname.

## Expected display behavior

`Demo Rotation` alternates every 10 seconds between:

- a black screen with red, green, blue, and white rectangles;
- an eight-position yellow-circle animation.

## Remote JPEG

Place a baseline JPEG in Home Assistant, for example:

```text
/config/www/wall_display/current.jpg
```

Home Assistant serves that file at:

```text
http://homeassistant.local:8123/local/wall_display/current.jpg
```

Enter the URL in `Remote JPEG URL`, press `Refresh Remote JPEG`, and confirm
that `Remote JPEG Status` changes from `Downloading` to `Loaded`.

## BLE protection

- `Start BLE Setup` turns the backlight off before BLE starts.
- The Backlight control cannot re-enable the panel while BLE is active.
- `Stop BLE Setup` disables BLE and restores the prior display state.

## Completed physical results

- USB installation: pass
- Device Builder fixed-hostname tracking: pass
- Wi-Fi: pass
- encrypted Native API: pass
- device-specific OTA password: pass
- wireless OTA installation: pass
- RGBW static display: pass
- eight-frame animation: pass
- demo rotation: pass
- local remote JPEG: pass
- protected BLE Start/Stop behavior: pass
- visible flicker during protected BLE operation: none

No further S3 hardware test is required for the current release candidate.
