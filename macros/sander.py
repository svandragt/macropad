# SPDX-FileCopyrightText: 2023 Sander an Dragt
#
# SPDX-License-Identifier: MIT

# MACROPAD Sander's preferred configuration

from adafruit_hid.keycode import Keycode

# REQUIRED dict, must be named 'app'
app = {
    'name' : 'elementary OS',
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000040, '<<win', [Keycode.ALT, Keycode.SHIFT, Keycode.TAB]),
        (0x000040, 'win>>', [Keycode.ALT, Keycode.TAB]),
        (0x400040, 'Multi', [Keycode.COMMAND]),
        # 2nd row ----------
        (0x202000, 'Hide', [Keycode.COMMAND, 'h']),
        (0x202000, 'H.Othr', [Keycode.COMMAND, Keycode.SHIFT, 'h']),
        (0x002020, 'AI', [Keycode.COMMAND, 'i']),
        # 3rd row ----------
        (0x101010, 'Term', [Keycode.COMMAND, 't']),
        (0x101010, 'Notes ', [Keycode.COMMAND, 'n']),
        (0x101010, 'Launch', [Keycode.CONTROL, Keycode.ALT, Keycode.COMMAND, ' ']),
        # 4th row ----------
        (0x000020, 'Sel.All', [Keycode.CONTROL, 'a']),
        (0x004000, 'Copy', [Keycode.CONTROL, 'c']),
        (0x004000, 'Paste', [Keycode.CONTROL, 'v']),
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'q']) # Quit app
    ]
}
