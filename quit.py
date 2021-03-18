import time
from source import QUIT_FILE


def main():
    with open(QUIT_FILE, "w"):
        pass
    print("Stopping...")
    time.sleep(0.5)
    print("Done")
    time.sleep(1)


if __name__ == '__main__':
    main()
