import webview
import multiprocessing
import server


def start_server():
    print("Starting Server")
    process = multiprocessing.Process(target=server.start)
    process.start()
    return process


def start_webview():
    print("Starting Webview")
    webview.create_window("Test", f"http://localhost:{server.PORT}/")
    webview.start()


def main():
    server_process = start_server()

    server_process.terminate()
    print("App Exit")


if __name__ == '__main__':
    main()
