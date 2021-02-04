import os
import json
import source
from source.macros import macro


class Profile:
    def __init__(self, profile_data):
        self.name = profile_data["name"]
        self.description = profile_data["description"]
        self.profile_macros = self.get_macros(profile_data["macros"])
        self.session = SessionData()

    def get_macros(self, macro_data):
        macros = []
        for individual_macro_data in macro_data:
            macros.append(macro.get_macro_from_json(self, individual_macro_data))
        return macros

    def load(self):
        for profile_macro in self.profile_macros:
            profile_macro.activate()

    def unload(self):
        for profile_macro in self.profile_macros:
            profile_macro.deactivate()


class SessionData:
    def __init__(self, data=None):
        if data is None:
            data = {}
        self.__dict__["data"] = data

    def __getattr__(self, item):
        return self.__dict__["data"][item]

    def __setattr__(self, key, value):
        self.__dict__["data"][key] = value


def verify_project_root_exists():
    for dir_path in source.PROJECT_DIRS:
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

    for file_path, default_contents in source.PROJECT_FILES.items():
        if not os.path.exists(file_path):
            write_json(file_path, default_contents, indent=4)


def get_profile(profile_name):
    file_path = os.path.join(source.PROFILES_DIR, f"{profile_name}.json")
    profile_json = read_json(file_path)
    return Profile(profile_json)


def get_default_profile():
    return get_profile("default")


def get_current_profile():
    settings = get_settings()
    current_profile_name = settings.get("current_profile", "default")
    return get_profile(current_profile_name)


def get_settings():
    return read_json(source.SETTINGS_FILE)


def read_json(file_path):
    with open(file_path) as read_file:
        contents = json.load(read_file)
    return contents


def write_json(file_path, contents, **kwargs):
    with open(file_path, "w") as write_file:
        json.dump(contents, write_file, **kwargs)
