import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

# Your actual pins from the schematic
PINS = [
    board.GP26,
    board.GP27,
    board.GP28,
    board.GP29,
    board.GP6,
    board.GP7
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [
        KC.A,
        KC.B,
        KC.C,
        KC.D,
        KC.E,
        KC.F,
    ]
]

if __name__ == '__main__':
    keyboard.go()
