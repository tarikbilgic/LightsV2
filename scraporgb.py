import openrgb
import openrgb.utils as oru
from openrgb.utils import RGBColor
import time

client = openrgb.OpenRGBClient()
# print(client)

devices = client.devices
print(devices)
a = devices[0]
b = devices[1]

print(b.name)
print(b.modes)
print(b.active_mode)

COLORS = {
    "red": RGBColor(255, 0, 0),
    "green": RGBColor(0, 255, 0),
    "blue": RGBColor(0, 0, 255),
    "white": RGBColor(255, 255, 255),
}


# a.set_mode("direct")
# a.set_color(COLORS["red"], fast=False)
# b.set_mode("direct")
# b.set_color(COLORS["red"], fast=False)
# time.sleep(5)

a.set_colors([COLORS["red"]] * len(a.leds), fast=False)
time.sleep(2)
print(b.colors)


for led in b.leds:
    led.set_color(COLORS["red"], fast=False)

print(len(b.leds))
print(b.zones)
print(client.comms._protocol_version)


def set_device_color(device, color):
    for led in device.leds:
        if COLORS.get(color) == None:
            print("Invalid Color")
        else:
            led.set_color(COLORS[color], fast=False)


for d in client.devices:
    set_device_color(d, "blue")



# Create the client: openrgb.OpenRGBClient().
# Get the devices from client.devices.
# Loop over a device’s .leds.
# Call set_color(RGBColor(r, g, b), fast=False) on each LED.