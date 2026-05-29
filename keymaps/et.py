"""Estonian (ISO) keyboard layout. HID usage IDs from the USB HID Usage Tables."""

MODIFIERS = {
    "CTRL": 0x01,
    "CONTROL": 0x01,
    "SHIFT": 0x02,
    "ALT": 0x04,
    "ALTGR": 0x40,   # Right Alt — required for many Estonian symbols
    "GUI": 0x08,
    "WINDOWS": 0x08,
    "COMMAND": 0x08,
}

_SHIFT = MODIFIERS["SHIFT"]
_ALTGR = MODIFIERS["ALTGR"]

KEYS = {
    # a–z, A–Z (alphabetic positions identical to US QWERTY)
    **{chr(c): (0x04 + c - ord("a"), 0) for c in range(ord("a"), ord("z") + 1)},
    **{chr(c): (0x04 + c - ord("A"), _SHIFT) for c in range(ord("A"), ord("Z") + 1)},

    # Top row digits with their shifted and AltGr symbols
    "1": (0x1E, 0), "!": (0x1E, _SHIFT),
    "2": (0x1F, 0), '"': (0x1F, _SHIFT), "@": (0x1F, _ALTGR),
    "3": (0x20, 0), "#": (0x20, _SHIFT), "£": (0x20, _ALTGR),
    "4": (0x21, 0), "¤": (0x21, _SHIFT), "$": (0x21, _ALTGR),
    "5": (0x22, 0), "%": (0x22, _SHIFT), "€": (0x22, _ALTGR),
    "6": (0x23, 0), "&": (0x23, _SHIFT),
    "7": (0x24, 0), "/": (0x24, _SHIFT), "{": (0x24, _ALTGR),
    "8": (0x25, 0), "(": (0x25, _SHIFT), "[": (0x25, _ALTGR),
    "9": (0x26, 0), ")": (0x26, _SHIFT), "]": (0x26, _ALTGR),
    "0": (0x27, 0), "=": (0x27, _SHIFT), "}": (0x27, _ALTGR),

    # Right of 0: + ? \
    "+": (0x2D, 0), "?": (0x2D, _SHIFT), "\\": (0x2D, _ALTGR),
    # 0x2E is the ´/` dead-key — omitted (dead keys can't be sent as single chars)

    # Estonian letters on the right side of the keyboard
    "ü": (0x2F, 0), "Ü": (0x2F, _SHIFT),
    "õ": (0x30, 0), "Õ": (0x30, _SHIFT), "§": (0x30, _ALTGR),
    "ö": (0x33, 0), "Ö": (0x33, _SHIFT),
    "ä": (0x34, 0), "Ä": (0x34, _SHIFT), "^": (0x34, _ALTGR),

    # Key right of Ä (ISO key 0x31): ' * ½
    "'": (0x31, 0), "*": (0x31, _SHIFT), "½": (0x31, _ALTGR),

    # Bottom row punctuation
    ",": (0x36, 0), ";": (0x36, _SHIFT),
    ".": (0x37, 0), ":": (0x37, _SHIFT),
    "-": (0x38, 0), "_": (0x38, _SHIFT),

    # ISO Non-US backslash key (left of Z): < > |
    "<": (0x64, 0), ">": (0x64, _SHIFT), "|": (0x64, _ALTGR),

    # š, ž via AltGr + S / Z (and shifted variants)
    "š": (0x16, _ALTGR), "Š": (0x16, _ALTGR | _SHIFT),
    "ž": (0x1D, _ALTGR), "Ž": (0x1D, _ALTGR | _SHIFT),

    # Whitespace
    " ": (0x2C, 0),
    "\t": (0x2B, 0),
    "\n": (0x28, 0),
    "\r": (0x28, 0),

    # Named keys (position-based — same HID codes as US)
    "ENTER": (0x28, 0), "RETURN": (0x28, 0),
    "ESC": (0x29, 0), "ESCAPE": (0x29, 0),
    "BACKSPACE": (0x2A, 0), "TAB": (0x2B, 0), "SPACE": (0x2C, 0),
    "CAPSLOCK": (0x39, 0),
    "F1": (0x3A, 0), "F2": (0x3B, 0), "F3": (0x3C, 0), "F4": (0x3D, 0),
    "F5": (0x3E, 0), "F6": (0x3F, 0), "F7": (0x40, 0), "F8": (0x41, 0),
    "F9": (0x42, 0), "F10": (0x43, 0), "F11": (0x44, 0), "F12": (0x45, 0),
    "PRINTSCREEN": (0x46, 0), "SCROLLLOCK": (0x47, 0), "PAUSE": (0x48, 0),
    "INSERT": (0x49, 0), "HOME": (0x4A, 0), "PAGEUP": (0x4B, 0),
    "DELETE": (0x4C, 0), "DEL": (0x4C, 0), "END": (0x4D, 0), "PAGEDOWN": (0x4E, 0),
    "RIGHT": (0x4F, 0), "LEFT": (0x50, 0), "DOWN": (0x51, 0), "UP": (0x52, 0),
}
