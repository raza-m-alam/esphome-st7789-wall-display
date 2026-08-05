# End-user Device Builder installation test

This test verifies the manual DIY installation path and, specifically, that
ESPHome Device Builder creates and stores unique local credentials for the
imported device.

Do not delete the known-good hardware-test configurations until this entire
procedure passes.

## What this test uses

Download this single file:

```text
install/st7789-wall-display-s3.yaml
```

The file is self-contained and has no Wi-Fi SSID, Wi-Fi password, API key, OTA
password, fallback-access-point password, or `!secret` reference.

## Import the configuration

1. Open ESPHome Device Builder in Home Assistant.
2. Select the control for creating a new device.
3. Choose **Import from File**.
4. Select `st7789-wall-display-s3.yaml`.
5. Open the imported device in the editor.

Do not choose **Empty Configuration**, and do not create a second Wi-Fi, API,
or OTA component. The imported file already contains one empty instance of
each component so Device Builder can configure those existing components.

## Configure local credentials in Device Navigator

Use Device Navigator rather than manually pasting credentials into YAML.

### Wi-Fi

1. Open the existing **Wi-Fi** component.
2. Add only the primary network for this first test.
3. Let Device Builder create or select the local secret names for the SSID and
   password.
4. Save the component.

For this baseline test, do not add both top-level `ssid` and `networks`. A
single-network configuration should use one form only. Backup networking can
be tested after the import path succeeds.

### Native API

1. Open the existing **Native API** component.
2. Enable API encryption.
3. Use Device Builder's generate/store control rather than typing a key.
4. Record only the generated secret *name*, not the secret value.
5. Confirm that the secret name is unique to this imported device.

### ESPHome OTA

1. Open the existing **ESPHome OTA** component.
2. Enable password protection.
3. Use Device Builder's generate/store control rather than typing a password.
4. Record only the generated secret *name*, not the secret value.
5. Confirm that the OTA secret name differs from the API secret name and is
   unique to this imported device.

## Validate before installing

1. Run **Validate**.
2. Confirm that there is no error about using `ssid` together with `networks`.
3. Confirm that there are no missing-secret errors.
4. Confirm that there is exactly one Native API component and one ESPHome OTA
   component.

Stop and preserve the validation output if any of those checks fail.

## Initial USB installation

1. Connect the ESP32-S3 N16R8 board by its USB serial/JTAG port.
2. Select **Install** for the imported device.
3. Choose the connected USB device or the browser-based USB installation
   option exposed by Device Builder.
4. Complete the installation.
5. Do not delete the previous known-good YAML.

## Expected physical result

The display should show:

1. black background;
2. red rectangle at the top;
3. green rectangle in the middle;
4. blue rectangle at the bottom.

The startup log should confirm:

- ESP32-S3;
- 8 MB PSRAM available;
- 170x320 ST7789V;
- GPIO12 clock and GPIO11 MOSI;
- GPIO10 chip select;
- GPIO9 data/command;
- GPIO13 reset;
- GPIO14 backlight;
- 10 MHz SPI;
- BGR color order;
- color inversion enabled;
- full 108,800-byte framebuffer;
- Wi-Fi connected;
- encrypted API enabled;
- OTA password configured.

## Home Assistant and OTA checks

1. Confirm Home Assistant discovers the device.
2. Add it using the generated API encryption key if Home Assistant does not
   complete discovery automatically.
3. Confirm the Backlight, Restart, Safe Mode, Start BLE Setup, Stop BLE Setup,
   and Test Pattern entities appear.
4. Perform one OTA installation from the imported Device Builder entry.
5. Confirm the OTA installation uses the device-specific OTA credential and
   completes without USB.

## What to capture

Return the following without exposing secret values:

- the final imported YAML;
- the generated Wi-Fi, API, and OTA secret names;
- the validation output;
- the startup log;
- whether the display colors and geometry are correct;
- whether Home Assistant discovery succeeds;
- whether the first OTA update succeeds.

## Final published installation path

The manual import above is the source-install path for a user assembling a bare
board. The preferred public release path will be different:

1. the user flashes a published factory firmware image;
2. the user provisions Wi-Fi through BLE or serial Improv;
3. ESPHome Device Builder discovers the project;
4. the user selects **Take Control**;
5. `dashboard_import` creates a minimal local configuration referencing the
   public GitHub package;
6. Device Builder stores the user's unique credentials locally.

In that preferred path, the user does not manually download and import the YAML
package.
