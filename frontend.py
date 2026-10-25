# Designed with https://visualtkinter.com - paste this file into File > Import there to edit it visually
# Requires ttkbootstrap:  pip install ttkbootstrap
import tkinter as tk
import ttkbootstrap as ttkb
import powerswitch
import colorchanger
import color
import brightness
from tkinter import colorchooser
import rgbcontrol
import RGBbrightness as rb
import rgbpower


def styled(name, **options):

    ttkb.Style().configure(name, **options)
    return name


def styled(name, **options):
    """Define a named ttk style and return its name.

    ttk widgets take their colours and fonts from a style rather than from
    constructor options, so a per-widget look needs a per-widget style."""
    ttkb.Style().configure(name, **options)
    return name


THEME_BG = "#2C2C2A"
THEME_FG = "#2C2C2A"
THEME_ACCENT = "#2a7de1"
THEME_ACCENT_FG = "#ffffff"
THEME_FIELD_BG = "#ffffff"
THEME_FONT = ("Helvetica", 10)


def apply_theme(root):
    """Layer the project theme over the ttkbootstrap theme. Per-widget
    styles override these; the base theme still supplies hover and focus."""
    style = ttkb.Style()
    style.configure(".", background=THEME_BG, foreground=THEME_FG, font=THEME_FONT)
    style.configure("TButton", background=THEME_ACCENT, foreground=THEME_ACCENT_FG)
    style.configure("TLabel", background=THEME_BG)
    style.configure("TMenubutton", background=THEME_ACCENT, foreground=THEME_ACCENT_FG)
    for field in ("TEntry", "TCombobox", "TSpinbox"):
        style.configure(field, fieldbackground=THEME_FIELD_BG, foreground=THEME_FG)
    style.configure("Treeview", fieldbackground=THEME_FIELD_BG)
    root.configure(background=THEME_BG)
    # Listbox, Text and Canvas are classic tkinter widgets — they read the
    # option database rather than the ttk style.
    root.option_add("*Listbox.background", THEME_FIELD_BG)
    root.option_add("*Listbox.foreground", THEME_FG)
    root.option_add("*Text.background", THEME_FIELD_BG)
    root.option_add("*Text.foreground", THEME_FG)
    root.option_add("*font", THEME_FONT)


class Application:
    def __init__(self, root):
        self.root = root
        self.current_colour = (255,255,255)
        root.title("Lights V2")
        root.geometry("500x250")
        apply_theme(root)

        self.button1 = ttkb.Button(root, text="⏻ power switch", command=self.on_button1, style=styled("button1.TButton", font=("Helvetica", 10, "bold", ), bordercolor="#2C2C2A", lightcolor="#2C2C2A", darkcolor="#2C2C2A", focuscolor="#2C2C2A"))
        self.button1.place(x=184, y=60, width=284, height=40)

        self.Brightness = ttkb.Scale(root, from_=100, to=1, orient="vertical", style=styled("Brightness.dark.Vertical.TScale", background=THEME_BG))
        self.Brightness.place(x=71, y=50, width=30, height=170)
        self.Brightness.bind("<ButtonRelease-1>", self.on_brightness_release)

        self.colorchooser = ttkb.Button(root, text="Color Wheel", command=self.pick_colour, style=styled("colorchooser.TButton", background="#2C2C2A"))
        self.colorchooser.place(x=184, y=178, width=284, height=30)

        self.separator2 = ttkb.Separator(root, orient="vertical", style=styled("separator2.Vertical.TSeparator", background="#d3d1c7"))
        self.separator2.place(x=16, y=10, width=1, height=224)

        self.separator3 = ttkb.Separator(root, orient="vertical", style=styled("separator3.Vertical.TSeparator", background="#d3d1c7"))
        self.separator3.place(x=155, y=10, width=1, height=224)

        self.separator4 = ttkb.Separator(root, orient="horizontal", style=styled("separator4.Horizontal.TSeparator", background="#d3d1c7"))
        self.separator4.place(x=16, y=10, width=140, height=1)

        self.label1 = ttkb.Label(root, text="Brightness", anchor="center", style=styled("label1.TLabel", foreground="#E9E6DD"))
        self.label1.place(x=36, y=18, width=100, height=22)

        self.separator6 = ttkb.Separator(root, orient="horizontal", style=styled("separator6.Horizontal.TSeparator", background="#d3d1c7"))
        self.separator6.place(x=168, y=10, width=316, height=1)

        self.separator7 = ttkb.Separator(root, orient="horizontal", style=styled("separator7.Horizontal.TSeparator", background="#d3d1c7"))
        self.separator7.place(x=168, y=115, width=316, height=1)

        self.separator8 = ttkb.Separator(root, orient="vertical", style=styled("separator8.Vertical.TSeparator", background="#d3d1c7"))
        self.separator8.place(x=168, y=10, width=1, height=106)

        self.separator9 = ttkb.Separator(root, orient="vertical", style=styled("separator9.Vertical.TSeparator", background="#d3d1c7"))
        self.separator9.place(x=483, y=10, width=1, height=106)

        self.label2 = ttkb.Label(root, text="Power", anchor="center", style=styled("label2.TLabel", foreground="#E9E6DD"))
        self.label2.place(x=276, y=18, width=100, height=22)

        self.label3 = ttkb.Label(root, text="Colour", anchor="center", style=styled("label3.TLabel", foreground="#E9E6DD"))
        self.label3.place(x=276, y=136, width=100, height=22)

        self.separator10 = ttkb.Separator(root, orient="horizontal", style=styled("separator10.Horizontal.TSeparator", background="#d3d1c7"))
        self.separator10.place(x=168, y=233, width=316, height=1)

        self.separator11 = ttkb.Separator(root, orient="horizontal", style=styled("separator11.Horizontal.TSeparator", background="#d3d1c7"))
        self.separator11.place(x=168, y=128, width=316, height=1)

        self.separator12 = ttkb.Separator(root, orient="vertical", style=styled("separator12.Vertical.TSeparator", background="#d3d1c7"))
        self.separator12.place(x=168, y=128, width=1, height=106)

        self.separator13 = ttkb.Separator(root, orient="vertical", style=styled("separator13.Vertical.TSeparator", background="#d3d1c7"))
        self.separator13.place(x=483, y=128, width=1, height=106)

        self.separator14 = ttkb.Separator(root, orient="horizontal", style=styled("separator14.Horizontal.TSeparator", background="#d3d1c7"))
        self.separator14.place(x=16, y=233, width=140, height=1)

    def on_brightness_release(self, event):

        level = self.Brightness.get()
        brightness.set_brightness(level)

        print(level)
        print(self.current_colour, level)
        r = self.current_colour[0]
        g = self.current_colour[1]
        b = self.current_colour[2]
        sr, sg, sb = rb.scaling(level, r=r, g=g , b=b)
        for d in rgbcontrol.devices:
            rgbcontrol.set_rgb_color(d, sr, sg, sb)

    def on_button1(self):
        state = powerswitch.powerswitch()
        level = self.Brightness.get()
        r = self.current_colour[0]
        g = self.current_colour[1]
        b = self.current_colour[2]
        sr, sg, sb = rb.scaling(level, r=r, g=g, b=b)
        for d in rgbcontrol.devices:
            rgbpower.power(d, state, sr, sg, sb) 


    def pick_colour(self):
        result = colorchooser.askcolor()
        if result[0] is None:
            return
        else:
            r, g, b = result[0]
            level = self.Brightness.get() 
            self.current_colour = r, g, b
            packed = color.rgb_to_int(r, g, b )
            test = colorchanger.send_colour(packed)
            sr, sg, sb = rb.scaling(level, r, g, b)



        for d in rgbcontrol.devices:
            rgbcontrol.set_rgb_color(d, sr, sg, sb)



if __name__ == "__main__":
    root = ttkb.Window(themename="litera")
    app = Application(root)
    root.mainloop()
