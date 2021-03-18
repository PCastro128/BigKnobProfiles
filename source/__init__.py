import os

PROJECT_DATA_ROOT = os.path.join("C:\\", "Users", os.getlogin(), "AppData", "Local", "BigKnobProfiles")

# Profiles
PROFILES_DIR = os.path.join(PROJECT_DATA_ROOT, "profiles")
DEFAULT_PROFILE_FILE = os.path.join(PROFILES_DIR, "default.json")

SETTINGS_FILE = os.path.join(PROJECT_DATA_ROOT, "settings.json")
DEFAULT_SETTINGS_DATA = {
    "current_profile": "default",
    "available_profiles": ["default"]
}

PROJECT_DIRS = [PROJECT_DATA_ROOT, PROFILES_DIR]

# Status

STATUS_FILE = os.path.join(PROJECT_DATA_ROOT, "status.json")
QUIT_FILE = os.path.join(PROJECT_DATA_ROOT, "quit")
