import board

from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.modules.modtap import ModTap
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.RGB import RGB

keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()
layers = Layers()
modtap = ModTap()
mediakeys = MediaKeys()

split = Split(use_pio=True)

encoder_handler.pins = ((keyboard.encoder_b, keyboard.encoder_a, None, False))

keyboard.modules = [layers, split, encoder_handler, modtap, mediakeys]

# Cleaner key names
XXXXXXX = KC.NO
UNDO = KC.LCTL(KC.Z)
CUT = KC.LCTL(KC.X)
COPY = KC.LCTL(KC.C)
PASTE = KC.LCTL(KC.V)
LSTRT = KC.LCTL(KC.HOME)
LEND = KC.LCTL(KC.END)
BACK = KC.LALT(KC.LEFT)
NEXT = KC.LALT(KC.RGHT)
LBSPC = KC.LCTL(KC.BSPC)
LOWER = KC.MO(1)
RAISE = KC.MO(2)

keyboard.keymap = [
    [  # QWERTY
        # HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----#ENCODER--#ENCODER--# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----
        KC.GRV,   KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,                                            KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,    KC.GRV,
        KC.ESC,   KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,                                             KC.Y,     KC.U,     KC.I,     KC.O,     KC.P,     KC.BSPC,
        KC.TAB,   KC.A,     KC.S,     KC.D,     KC.F,     KC.G,                                             KC.H,     KC.J,     KC.K,     KC.L,     KC.SCLN,  KC.QUOT,
        KC.LSFT,  KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,                                             KC.N,     KC.M,     KC.COMM,  KC.DOT,   KC.SLSH,  KC.RSFT,
                            KC.LGUI,  KC.LALT,  KC.LCTL,  LOWER,    KC.SPC,   KC.MUTE,  KC.MPLY,  KC.ENT,   RAISE,    KC.RCTL,  KC.RALT,  KC.RGUI,
    ],
    [  #LOWER
        # HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----#ENCODER--#ENCODER--# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----
        XXXXXXX,  KC.F1,    KC.F2,    KC.F3,    KC.F4,    KC.F5,                                            KC.F6,    KC.F7,    KC.F8,    KC.F9,    KC.F10,   KC.F11,
        KC.GRV,   KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,                                            KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,    KC.F12,
        XXXXXXX,  KC.EXLM,  KC.AT,    KC.HASH,  KC.DLR,   KC.PERC,                                          KC.CIRC,  KC.AMPR,  KC.ASTR,  KC.LPRN,  KC.RPRN,  KC.PIPE,
        XXXXXXX,  KC.EQL,   KC.MINS,  KC.PLUS,  KC.LCBR,  KC.RCBR,                                          KC.LBRC,  KC.RBRC,  KC.SCLN,  KC.COLN,  KC.BSLS,  XXXXXXX,
                            XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
    ],
    [  #RAISE
        # HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----#ENCODER--#ENCODER--# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----
        XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,                                          XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
        XXXXXXX,  KC.INS,   KC.PSCR,  KC.APP,   XXXXXXX,  XXXXXXX,                                          KC.PGUP,  BACK,     KC.UP,    NEXT,     LBSPC,    KC.BSPC,
        XXXXXXX,  KC.LALT,  KC.LCTL,  KC.LSFT,  XXXXXXX,  KC.CAPS,                                          KC.PGDN,  KC.LEFT,  KC.DOWN,  KC.RGHT,  KC.DEL,   KC.BSPC,
        XXXXXXX,  UNDO,     CUT,      COPY,     PASTE,    XXXXXXX,                                          XXXXXXX,  LSTRT,    XXXXXXX,  LEND,     XXXXXXX,  XXXXXXX,
                            XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
    ]
]

encoder_handler.map = (
    ((KC.VOLD, KC.VOLU),),  # base layer
    ((KC.VOLD, KC.VOLU),),  # Raise
    ((KC.VOLD, KC.VOLU),),  # Lower
)

# rgb
rgb = RGB(keyboard.rgb_pixel_pin, num_pixels=36, hue_default=127, sat_default=255, val_default=255)
keyboard.extensions.append(rgb)

keyboard.debug_enabled = True

if __name__ == '__main__':
    keyboard.go()
