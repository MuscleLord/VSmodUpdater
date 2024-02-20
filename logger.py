import os, sys
from datetime import datetime as dt
from contextlib import redirect_stderr


class LogDirHandle:

    LOG_PATH = ".\\Logs"

    def __init__(self) -> None:

        if not os.path.isdir(self.LOG_PATH):
            os.mkdir(self.LOG_PATH)


class Error:
    def __init__(self, errmsg: str):
        super().__init__()
        try:
            LogDirHandle()
            self.path = LogDirHandle.LOG_PATH

            with open(
                f"{self.path}\\errors.log", "a", encoding="utf-8"
            ) as stderr, redirect_stderr(stderr):
                print(
                    f'{dt.today().strftime("%Y-%m-%d %H:%M:%S")} : {errmsg}',
                    file=sys.stderr,
                )
        except Exception as e:
            print("Something went wrong writing log: ", e)


class Events:
    def __init__(self, eventmsg: str):
        super().__init__()
        try:
            LogDirHandle()
            self.path = LogDirHandle.LOG_PATH

            with open(
                f"{self.path}\\main.log", "a", encoding="utf-8"
            ) as stderr, redirect_stderr(stderr):
                print(
                    f'{dt.today().strftime("%Y-%m-%d %H:%M:%S")} : {eventmsg}',
                    file=sys.stderr,
                )
        except Exception as e:
            print("Something went wrong writing log: ", e)
