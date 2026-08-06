# Installation

The primary ESP32-S3 profile is:

```text
install/st7789-wall-display-s3.yaml
```

## First installation

1. In Home Assistant, open **ESPHome Device Builder**.
2. Select **Create device**, then **Import from File**.
3. Import `st7789-wall-display-s3.yaml`.
4. In Device Navigator, add the local Wi-Fi SSID and password.
5. Enable Native API encryption and generate a unique key for the device.
6. Add a unique ESPHome OTA password.
7. Validate the configuration.
8. Connect the ESP32-S3 by USB and perform the first installation.
9. Use OTA for subsequent updates.

The profile uses a fixed hostname:

```yaml
name: "st7789-wall-display-s3"
name_add_mac_suffix: false
```

This keeps the Device Builder entry and the hostname announced by the device
in sync after a manual import.

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

## BLE setup

- `Start BLE Setup` turns the backlight off before BLE starts.
- The Backlight control cannot illuminate the panel while BLE is active.
- `Stop BLE Setup` disables BLE and restores the prior display state.

Physical validation results are recorded in `docs/validation.md`.
