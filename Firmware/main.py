import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.rotary_encoder import RotaryEncoder

keyboard = KMKKeyboard()

PINS = [
    board.GP26,
    board.GP27,
    board.GP28,
    board.GP29,
    board.GP6,
    board.GP7,
    board.GP2,
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

encoder = RotaryEncoder(
    pin_a=board.GP0,
    pin_b=board.GP1,
    ccw=KC.VOLD,
    cw=KC.VOLU,
)

keyboard.modules.append(encoder)

keyboard.keymap = [
    [
        KC.A,
        KC.B,
        KC.C,
        KC.D,
        KC.E,
        KC.F,
        KC.MUTE,
    ]
]

if __name__ == '__main__':
    keyboard.go()
