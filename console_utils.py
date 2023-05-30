import os
import re
import sys
import time

# Regular expressions for RGB color codes
SHORT_RGB_REGEX = re.compile(r"^#([0-9a-fA-F]{3})$")
LONG_RGB_REGEX = re.compile(r"^#([0-9a-fA-F]{6})$")

# Regular expression for ANSI escape sequences
ANSI_ESCAPE_REGEX = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

# Function to print text slowly with optional delay and end character
def slowprint(object, delay=0.01, end="\n"):
    text = str(object)
    text = text + end

    # Splitting ANSI escape codes from the text
    ansi_codes = ANSI_ESCAPE_REGEX.findall(text)
    text = ANSI_ESCAPE_REGEX.split(text)

    ansi_code_index = 0
    for i in range(len(ansi_codes)):
        # Adjusting the index to account for ANSI escape codes
        ansi_code_index += len(text[i])
        ansi_codes[i] = (ansi_codes[i], ansi_code_index)
    text = "".join(text)

    printed = 0
    length = len(text)
    timer = time.time()

    while printed < length:
        to_print = int((time.time() - timer) / delay)
        timer += to_print * delay

        # Printing characters and inserting ANSI escape codes when necessary
        for i in range(to_print):
            while ansi_codes and ansi_codes[0][1] == printed:
                sys.stdout.write(ansi_codes.pop(0)[0])
                sys.stdout.flush()
            sys.stdout.write(text[printed])
            sys.stdout.flush()
            printed += 1

# Class for representing colors
class Color:
    def __init__(self, color):
        # Initializing color from RGB tuple
        if (
            isinstance(color, tuple)
            and all(isinstance(value, int) for value in color)
            and len(color) == 3
            and all(0 <= value <= 255 for value in color)
        ):
            self.r, self.g, self.b = color

        # Initializing color from long RGB code
        elif isinstance(color, str) and LONG_RGB_REGEX.match(color):
            self.r = int(color[1:3], 16)
            self.g = int(color[3:5], 16)
            self.b = int(color[5:7], 16)

        # Initializing color from short RGB code
        elif isinstance(color, str) and SHORT_RGB_REGEX.match(color):
            self.r = int(color[1], 16) * 0x11
            self.g = int(color[2], 16) * 0x11
            self.b = int(color[3], 16) * 0x11

        else:
            raise TypeError("Invalid color")

    # Get the RGB values of the color
    def get_rgb(self):
        return self.r, self.g, self.b

# Function to apply colors to text using ANSI escape sequences
def colorize(text, fg_color, bg_color=None):
    if not isinstance(fg_color, Color):
        fg_color = Color(fg_color)

    fg_style = f"\033[38;2;{';'.join(str(val) for val in fg_color.get_rgb())}m"

    if bg_color == None:
        bg_style = ""
    else:
        if not isinstance(bg_color, Color):
            bg_color = Color(bg_color)
        bg_style = f"\033[48;2;{';'.join(str(val) for val in bg_color.get_rgb())}m"

    reset_style = "\033[0m"

    return f"{fg_style}{bg_style}{text}{reset_style}"

# Required for ANSI initialization in some terminals
os.system("")
print("\033[0m", end="")
