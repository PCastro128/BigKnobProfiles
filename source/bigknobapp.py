import webview
import time
import multiprocessing

from source import server
from source.macros.bigknob import BigKnobKeyboard
from source.macros.profiles import verify_project_root_exists


def start_server():
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
        verify_project_root_exists()

    def start(self):
        self._create_hotkeys()
        while self.app_is_running:
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
        self.server_process.terminate()

    def stop(self):
        self.app_is_running = False
