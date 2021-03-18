import time

from source.status import get_status


def main():
    status = get_status()
    if time.time() < status["timestamp"] + status["lifespan"]:
        print("Status: \033[1m\033[92mOnline\033[0m")
        print(f"Session Number: {status['session_number']}")
    else:
        print("Status: \033[1m\033[91mOffline\033[0m")
    time.sleep(2)


if __name__ == '__main__':
    main()
