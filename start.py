import webview
import multiprocessing
import server
import keyboard
import time


def start_server():
    print("Starting Server")
    process = multiprocessing.Process(target=server.start)
    process.start()
    return process


def start_webview():
    print("Starting Webview")
    webview.create_window("Test", f"http://localhost:{server.PORT}/")
    webview.start()


def open_gui():
    server_process = start_server()
    start_webview()
    server_process.terminate()
    print("App Exit")


class App:
    def __init__(self):
        self.waiting = True

    def start(self):
        while True:
            if self.waiting:
                time.sleep(0.1)
            else:
                open_gui()
                self.waiting = True

    def stop_waiting(self):
        self.waiting = False


def main():
    macro_app = App()
    keyboard.add_hotkey("ctrl+f10", macro_app.stop_waiting)
    macro_app.start()


if __name__ == '__main__':
    main()
