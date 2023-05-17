import os
import re
import sys
import time


SHORT_RGB_REGEX = re.compile(r"^#([0-9a-fA-F]{3})$")
LONG_RGB_REGEX = re.compile(r"^#([0-9a-fA-F]{6})$")

ANSI_ESCAPE_REGEX = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")


def slowprint(object, delay=0.01, end="\n"):
    text = str(object)
    text = text + end

    ansi_codes = ANSI_ESCAPE_REGEX.findall(text)
    text = ANSI_ESCAPE_REGEX.split(text)

    ansi_code_index = 0
    for i in range(len(ansi_codes)):
        ansi_code_index += len(text[i])
        ansi_codes[i] = (ansi_codes[i], ansi_code_index)
    text = "".join(text)

    printed = 0
    length = len(text)
    timer = time.time()

    while printed < length:
        to_print = int((time.time() - timer) / delay)
        timer += to_print * delay

        for i in range(to_print):
            while ansi_codes and ansi_codes[0][1] == printed:
                sys.stdout.write(ansi_codes.pop(0)[0])
                sys.stdout.flush()
            sys.stdout.write(text[printed])
            sys.stdout.flush()
            printed += 1


class Color:
    def __init__(self, color):
        if (
            isinstance(color, tuple)
            and all(isinstance(value, int) for value in color)
            and len(color) == 3
            and all(0 <= value <= 255 for value in color)
        ):
            self.r, self.g, self.b = color

        elif isinstance(color, str) and LONG_RGB_REGEX.match(color):
            self.r = int(color[1:3], 16)
            self.g = int(color[3:5], 16)
            self.b = int(color[5:7], 16)

        elif isinstance(color, str) and SHORT_RGB_REGEX.match(color):
            self.r = int(color[1], 16) * 0x11
            self.g = int(color[2], 16) * 0x11
            self.b = int(color[3], 16) * 0x11

        else:
            raise TypeError("Invalid color")

    def get_rgb(self):
        return self.r, self.g, self.b


def colorize(text, fg_color, bg_color=None):
    if not isinstance(fg_color, Color):
        fg_color = Color(fg_color)

    fg_style = f"\033[38;2;{';'.join(str(val) for val in fg_color.get_rgb())}m"

    if bg_color == None:
        bg_style = ""
    else:
        if not isinstance(fg_color, Color):
            bg_color = Color(bg_color)
        bg_style = f"\033[48;2;{';'.join(str(val) for val in bg_color.get_rgb())}m"

    reset_style = "\033[0m"

    return f"{fg_style}{bg_style}{text}{reset_style}"


os.system("")  # required for ansi initialization
print("\033[0m", end="")
