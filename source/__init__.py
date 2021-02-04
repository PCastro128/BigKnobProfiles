import os

PROJECT_DATA_ROOT = os.path.join("C:\\", "Users", os.getlogin(), "AppData", "Local", "BigKnobProfiles")

PROFILES_DIR = os.path.join(PROJECT_DATA_ROOT, "profiles")
DEFAULT_PROFILE_FILE = os.path.join(PROFILES_DIR, "default.json")
DEFAULT_PROFILE_DATA = {
    "name": "Default",
    "description": "The default macro - multimedia controls",
    "macros": [
        {
            "name": "Volume Up",
            "type": "hotkey",
            "hotkey": "f13",
            "data": {
                "hotkey": "volume up"
            }
        },
        {
            "name": "Volume Down",
            "type": "hotkey",
            "hotkey": "f14",
            "data": {
                "hotkey": "volume down"
            }
        },
        {
            "name": "Toggle Audio Mute",
            "type": "hotkey",
            "hotkey": "f15",
            "data": {
                "hotkey": "volume mute"
            }
        },
        {
            "name": "Go to Previous Track",
            "type": "hotkey",
            "hotkey": "f16",
            "data": {
                "hotkey": "previous track"
            }
        },
        {
            "name": "Play/Pause Media",
            "type": "hotkey",
            "hotkey": "f17",
            "data": {
                "hotkey": "play/pause media"
            }
        },
        {
            "name": "Stop Media",
            "type": "hotkey",
            "hotkey": "f18",
            "data": {
                "hotkey": "stop media"
            }
        },
        {
            "name": "Skip Track",
            "type": "hotkey",
            "hotkey": "f19",
            "data": {
                "hotkey": "next track"
            }
        }
    ]
}

SETTINGS_FILE = os.path.join(PROJECT_DATA_ROOT, "settings.json")
DEFAULT_SETTINGS_DATA = {
    "current_profile": "default"
}

PROJECT_DIRS = [PROJECT_DATA_ROOT, PROFILES_DIR]
PROJECT_FILES = {DEFAULT_PROFILE_FILE: DEFAULT_PROFILE_DATA, SETTINGS_FILE: DEFAULT_SETTINGS_DATA}
