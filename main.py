#!/usr/bin/env python

from PIL import Image
import time
import random
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


from rgbmatrix import graphics
from rgbmatrix import RGBMatrix, RGBMatrixOptions


delay = 0.01
options = RGBMatrixOptions()
options.rows = 64
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.gpio_slowdown = 2
options.brightness = 20
options.hardware_mapping = "adafruit-hat"
options.daemon = False
options.drop_privileges = False

matrix = RGBMatrix(options=options)

offscreen_canvas = matrix.CreateFrameCanvas()

font = graphics.Font()
# font.LoadFont("fonts/10x20.bdf")
font.LoadFont("fonts/7x13.bdf")

textColor = graphics.Color(255, 255, 255)
pos = offscreen_canvas.width

# file = open("./text_to_scroll.txt", "r")
file = open("./ai_text.txt", "r")
lines = file.readlines()

out = []
while True:
    for line in lines:
        
        to_print = line[:-1]

        pos = offscreen_canvas.width

        length = 0
        elength = 0

        while pos + length + elength > 0:

            offscreen_canvas.Clear()
            length = graphics.DrawText(offscreen_canvas, font, pos, 20, textColor, to_print)
            pos -= 1
            time.sleep(delay)
            offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)


        matrix.Clear()
