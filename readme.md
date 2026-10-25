# LightsV2

A small desktop app that controls a **Govee H6047 light bar** (through the Govee Developer API) and the RGB lighting on a **Razer Ornata V3 X keyboard** and **Logitech G203 mouse** (through OpenRGB) from a single window, so they all change together.

## Features

- **Power switch**: turns the light bar on or off, and sets the keyboard and mouse to match (black when off, your colour at the current brightness when on).
- **Colour wheel**: pick any colour and it is applied to the light bar, keyboard and mouse.
- **Brightness slider**: sets the light bar's brightness and dims the keyboard and mouse to the same level.
- **Works without OpenRGB**: if OpenRGB isn't running, the app still opens and controls the Govee light on its own.

## Requirements

- Windows with Python 3 (developed on Python 3.14)
- A Govee API key (apply for one in the Govee Home app)
- [OpenRGB](https://openrgb.org/) installed, with its **SDK Server** started (default port 6742)
- Python packages:

```
pip install requests python-dotenv ttkbootstrap openrgb-python
```

## Setup

1. Put all the project files in one folder.
2. Create a file named `.env` in that folder (the name must start with the dot):

   ```
   API=your_govee_api_key
   sku=your_device_model_number
   device=your_device_id
   ```

   Keep this file private. If you use Git, add `.env` to `.gitignore`.
3. Open OpenRGB, go to the **SDK Server** tab and click **Start Server**.
4. Run the app:

   ```
   python frontend.py
   ```

## Project structure

| File | What it does |
| --- | --- |
| `frontend.py` | The tkinter / ttkbootstrap window: power button, brightness slider, colour wheel. |
| `powerswitch.py` | Turns the Govee light on or off and returns the new on/off state. |
| `brightness.py` | Sends a brightness value to the Govee light. |
| `colorchanger.py` | Sends a packed colour value to the Govee light. |
| `color.py` | Colour name dictionaries (packed integers for Govee, `(r, g, b)` tuples for OpenRGB) and `rgb_to_int`. |
| `rgbcontrol.py` | Connects to OpenRGB and sets every LED on a device to a colour. |
| `RGBbrightness.py` | `scaling()`: scales an `(r, g, b)` colour by a brightness percentage for the OpenRGB devices. |
| `rgbpower.py` | Turns an OpenRGB device off (black) or on (a given colour). |
| `scraporgb.py` | Scratch notes on how the OpenRGB library works. Not imported by the app. |

## How it works

- **Govee** is controlled with HTTP requests to the Govee Developer API. A colour is sent as one packed integer (`r * 65536 + g * 256 + b`).
- **OpenRGB** is controlled through its SDK server using the `openrgb-python` client. Colours are `RGBColor(r, g, b)` objects.
- The colour you pick is stored in the app as the full-brightness colour. When the slider moves, the stored colour is scaled by the slider percentage and sent to the keyboard and mouse. The Govee light uses its own brightness setting, so it always receives the original colour.
- The OpenRGB device colours are set one LED at a time, because the Logitech G203 ignored whole-device colour calls but responded to per-LED calls.

## Notes and known quirks

- **Govee rate limits.** The Govee API limits how many requests you can send per minute, which is why brightness is sent when the slider is released rather than continuously, and why there are no live colour sliders.
- **Power state at launch.** The app assumes the light is off when it starts. If the light bar is already on, the first press of the power button sends "on" and nothing visibly changes. Press it again.
- **OpenRGB must be running with the SDK server started** for the keyboard and mouse to respond. If it isn't, the app skips them and only controls the light bar.
- **Close Logitech G HUB** if the mouse doesn't respond, since it can take control of the lighting.

## Possible next steps

- Preset colour buttons or a dropdown
- Saved themes with a colour per device
- Merge the repeated "scale the stored colour and send it to every device" code into one method