import openrgb
import color
from openrgb.utils import RGBColor

client = openrgb.OpenRGBClient()

devices = client.devices

def set_rgb_color(device, r, g, b):
    colour = RGBColor(r,g,b)
    for led in device.leds:
        led.set_color(colour, fast=False)

def set_device_color(device, c):
    rgb = color.RGB_COLOURS.get(c)
    if rgb is None:
        print("Invalid Color")
        return

    set_rgb_color(device, *rgb)


if __name__ == "__main__":

    for d in devices:
        set_device_color(d, "red")
        set_device_color(d, "red")

