import webview
import time
import random
import multiprocessing

from source import server
from source.macros.bigknob import BigKnobKeyboard
from source.macros.profiles import select_default_profile
from source.status import check_for_quit_instruction, write_status, verify_project_files_exist


def start_server():
    if check_for_quit_instruction(SESSION):
        return
    print("Starting Server")
    process = multiprocessing.Process(target=server.start)
    process.start()
    return process


def start_web_view():
    print("Opening GUI")
    webview.create_window("Big Knob Profiles", f"http://localhost:{server.PORT}/",
                          on_top=True)
    webview.start()
    print("Closing GUI")


class BigKnobApp:
    def __init__(self):
        self.macros_active = True
        self.app_is_running = True
        self.server_process = start_server()
        self.bigknob_keyboard = BigKnobKeyboard(self)
        verify_project_files_exist(SESSION)
        select_default_profile()

    def start(self):
        if check_for_quit_instruction(SESSION):
            self.stop()
        self._create_hotkeys()
        while self.app_is_running:
            if check_for_quit_instruction(SESSION):
                self.stop()
            write_status(SESSION)
            self._main_loop()

    def _main_loop(self):
        if self.macros_active:
            time.sleep(0.1)
        else:
            start_web_view()
            self.on_gui_close()

    def on_gui_close(self):
        self._create_hotkeys()
        self.macros_active = True

    def open_gui(self):
        self._remove_hotkeys()
        self.macros_active = False

    def _create_hotkeys(self):
        self.bigknob_keyboard.load_current_profile()

    def _remove_hotkeys(self):
        self.bigknob_keyboard.unload_current_profile()

    def _deconstruct(self):
        self._remove_hotkeys()
        if self.server_process is not None:
            self.server_process.terminate()

    def stop(self):
        print("Stopping")
        time.sleep(1)
        self.app_is_running = False
        self._deconstruct()


class SessionData:
    def __init__(self, data=None):
        self.__dict__["session_number"] = random.randint(1000, 9999)
        if data is None:
            data = {}
        self.__dict__["data"] = data

    def get_session_number(self):
        return self.__dict__["session_number"]

    def __getattr__(self, item):
        if item not in self.__dict__["data"]:
            return None
        return self.__dict__["data"][item]

    def __setattr__(self, key, value):
        self.__dict__["data"][key] = value


SESSION = SessionData()
