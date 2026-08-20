# Installation

The primary ESP32-S3 profile is:

```text
install/st7789-wall-display-s3.yaml
```

## First installation

> **Do not flash the imported file until Native API encryption and an OTA
> password have been configured.** The file intentionally leaves those values
> empty so ESPHome Device Builder can create unique local secrets.

1. In Home Assistant, open **ESPHome Device Builder**.
2. Select **Create device**, then **Import from File**.
3. Import `st7789-wall-display-s3.yaml`.
4. Add the Wi-Fi SSID and password in Device Navigator.
5. Enable Native API encryption and generate a unique key.
6. Add a unique ESPHome OTA password.
7. Validate the configuration.
8. Connect the ESP32-S3 by USB and perform the first installation.
9. Use OTA for subsequent updates.

## Device name

The profile uses:

```yaml
name: "st7789-wall-display-s3"
name_add_mac_suffix: false
```

This keeps the imported Device Builder entry and the hostname announced by the
device in sync. Before importing another display, change the `name`
substitution so each device has a unique hostname.

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

The default example uses local HTTP. Keep the endpoint on a trusted LAN and do
not expose it directly to the internet.

## BLE setup

The tested board has no dedicated Improv authorization button, so the profile
uses `authorizer: none`. BLE is disabled during normal operation and is enabled
only for a limited setup window. Anyone within BLE range during that window
could submit Wi-Fi credentials.

- `Start BLE Setup` turns the backlight off before BLE starts.
- The Backlight control cannot illuminate the panel while BLE is active.
- `Stop BLE Setup` disables BLE and restores the previous display state.

Physical validation results are recorded in `TESTING.md` and
`docs/validation.md`.
