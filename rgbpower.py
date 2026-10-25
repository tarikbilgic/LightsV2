import openrgb
import rgbcontrol



def power(device, onoff, r, g, b):
    if onoff:
        colour = r , g, b
        rgbcontrol.set_rgb_color(device, *colour)
    else:
        r,g,b = 0,0,0
        rgbcontrol.set_rgb_color(device, r,g,b)


for d in rgbcontrol.devices:
    power(d, True, 255, 0, 0)    # should go dark