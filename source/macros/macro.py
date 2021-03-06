import keyboard
from abc import ABC, abstractmethod


class Macro(ABC):
    def __init__(self, name, macro_type, hotkey, data):
        self.name = name
        self.type = macro_type
        self.trigger_hotkey = hotkey
        self.data = data
        self.hotkey_remove_func = None

    @abstractmethod
    def trigger(self):
        pass

    def construct(self):
        pass

    def deconstruct(self):
        pass

    def activate(self):
        if len(keyboard.parse_hotkey(self.trigger_hotkey)[0]) == 1:
            remove_func = keyboard.on_release_key(self.trigger_hotkey, self.get_callback())
        else:
            remove_func = keyboard.add_hotkey(self.trigger_hotkey, self.get_callback(),
                                              trigger_on_release=True)
        self.hotkey_remove_func = remove_func
        self.construct()

    def deactivate(self):
        if self.hotkey_remove_func:
            self.hotkey_remove_func()
            self.deconstruct()
            self.hotkey_remove_func = None

    def get_callback(self):
        return lambda *args, **kwargs: self.trigger()

    def to_json(self):
        return {
            "name": self.name,
            "type": self.type,
            "hotkey": self.trigger_hotkey,
            "data": self.data
        }

    @staticmethod
    def from_json(macro_data):
        macro_type = macro_data["type"]
        if macro_data["type"] not in MACRO_TYPES:
            raise RuntimeError(f"Macro type '{macro_data['type']}' doesn't exist.")

        macro_class = MACRO_TYPES[macro_type]
        return macro_class(macro_data["name"], macro_data["type"], macro_data["hotkey"], macro_data["data"])


class HotkeyMacro(Macro):
    def trigger(self):
        keyboard.send(self.data["hotkey"])


MACRO_TYPES = {
    "hotkey": HotkeyMacro
}


def get_macro_callback(remap_key):
    return lambda *args, **kwargs: keyboard.send(remap_key)


def add_macro(src_hotkey, dst_hotkey):
    if len(keyboard.parse_hotkey(src_hotkey)[0]) == 1:
        return keyboard.on_release_key(src_hotkey, get_macro_callback(dst_hotkey))
    else:
        return keyboard.add_hotkey(src_hotkey, get_macro_callback(dst_hotkey),
                                   trigger_on_release=True)
