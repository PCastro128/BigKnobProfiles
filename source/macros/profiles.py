import os
import json
import source
from source.macros import macro
from source import common


class Profile:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.profile_macros = []

    def add_macros(self, macros):
        for individual_macro in macros:
            self.profile_macros.append(individual_macro)

    def load(self):
        for profile_macro in self.profile_macros:
            profile_macro.activate()

    def unload(self):
        for profile_macro in self.profile_macros:
            profile_macro.deactivate()

    def to_json(self):
        return {
            "name": self.name,
            "description": self.description,
            "macros": [individual_macro.to_json() for individual_macro in self.profile_macros]
        }

    @staticmethod
    def from_json(profile_data):
        new_profile = Profile(profile_data["name"], profile_data["description"])
        macros = []
        for individual_macro in profile_data["macros"]:
            macros.append(macro.Macro.from_json(individual_macro))
        new_profile.add_macros(macros)
        return new_profile


def get_profile(profile_name):
    file_path = os.path.join(source.PROFILES_DIR, f"{profile_name}.json")
    profile_json = common.read_json(file_path)
    return Profile.from_json(profile_json)


def get_default_profile():
    default_macros = [
        macro.HotkeyMacro("Volume Up", "hotkey", "f13", {"hotkey": "volume up"}),
        macro.HotkeyMacro("Volume Up", "hotkey", "f14", {"hotkey": "volume down"}),
        macro.HotkeyMacro("Volume Up", "hotkey", "f15", {"hotkey": "volume mute"}),
        macro.HotkeyMacro("Volume Up", "hotkey", "f16", {"hotkey": "previous track"}),
        macro.HotkeyMacro("Volume Up", "hotkey", "f17", {"hotkey": "play/pause media"}),
        macro.HotkeyMacro("Volume Up", "hotkey", "f18", {"hotkey": "stop media"}),
        macro.HotkeyMacro("Volume Up", "hotkey", "f19", {"hotkey": "next track"})
    ]
    default_profile = Profile("Default", "The default macro - multimedia controls")
    default_profile.add_macros(default_macros)
    return default_profile


def get_current_profile():
    settings = get_settings()
    current_profile_name = settings.get("current_profile", "default")
    return get_profile(current_profile_name)


def select_default_profile():
    select_profile("default")


def select_profile(profile_name):
    current_settings = get_settings()
    current_settings["current_profile"] = profile_name
    common.write_json(source.SETTINGS_FILE, current_settings, indent=4)


def get_settings():
    return common.read_json(source.SETTINGS_FILE)

