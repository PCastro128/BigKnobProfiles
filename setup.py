import os

SCRIPT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "run.pyw")
APPDATA_DIR = f'C:\\Users\\{os.getlogin()}\\AppData'
BAT_FILE = os.path.join(APPDATA_DIR, "Roaming", "Microsoft", "Windows", "Start Menu",
                        "Programs", "Startup", "bigknob.bat")


def main():
    if not os.path.exists(BAT_FILE):
        with open(BAT_FILE, "w+") as bat_file:
            bat_file.write(f'start "" {SCRIPT_FILE}')


if __name__ == '__main__':
    main()
