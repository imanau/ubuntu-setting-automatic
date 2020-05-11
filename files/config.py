# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *

define_modmap({
    Key.CAPSLOCK: Key.LEFT_CTRL,
})
define_multipurpose_modmap({
    Key.Q: [Key.Q, Key.RIGHT_META],
    Key.APOSTROPHE: [Key.APOSTROPHE, Key.RIGHT_ALT],
})
define_keymap(re.compile(r"^(?!Gnome-terminal)"), {
    K("Super-Backspace"): [K("Shift-Home"), K("Backspace")],
    K("Super-c"): [K("C-c")],
    K("Super-x"): [K("C-x")],
    K("Super-v"): [K("C-v")],
    K("Super-a"): [K("C-a")],
    K("Super-s"): [K("C-s")],
    K("Super-z"): [K("C-z")],
    K("Super-l"): [K("C-l")],
    K("Super-s"): [K("C-s")],
})
