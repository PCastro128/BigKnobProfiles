import keyboard
from source.macros import profiles


class BigKnobKeyboard:
    def __init__(self, app):
        self.app = app
        self.current_profile = None

    def load_current_profile(self):
        keyboard.add_hotkey("f19+f15", self.app.open_gui)
        self.current_profile = profiles.get_current_profile()
        self.current_profile.load()

    def load_meta_macros(self):
        pass

    def unload_current_profile(self):
        try:
            keyboard.unhook_all_hotkeys()
        except AttributeError:
            pass
        if self.current_profile:
            self.current_profile.unload()
            self.current_profile = None
