import os
import json
import time

import source
from source import QUIT_FILE, STATUS_FILE
from source import common
from source.macros.profiles import get_default_profile


def write_status(session):
    common.write_json(STATUS_FILE, generate_status_data(session), indent=4)


def generate_status_data(session):
    return {
        "timestamp": time.time(),
        "lifespan": 1,
        "session_number": session.get_session_number()
    }


def get_status():
    return common.read_json(STATUS_FILE)


def check_for_quit_instruction(session):
    if os.path.isfile(QUIT_FILE):
        os.remove(QUIT_FILE)
        return True

    status = get_status()
    if time.time() > status["timestamp"] + status["lifespan"]:
        return False
    if session.get_session_number() != status["session_number"]:
        return True

    return False


def verify_project_files_exist(session):
    for dir_path in source.PROJECT_DIRS:
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

    if not os.path.exists(source.SETTINGS_FILE):
        common.write_json(source.SETTINGS_FILE, source.DEFAULT_SETTINGS_DATA, indent=4)
    if not os.path.exists(source.DEFAULT_PROFILE_FILE):
        common.write_json(source.DEFAULT_PROFILE_FILE, get_default_profile().to_json(), indent=4)
    if not os.path.exists(source.STATUS_FILE):
        write_status(session)
