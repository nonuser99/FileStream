import sys
import pytz
import uvloop
import datetime
from config import LOG_FILE
from FileStream.Robot import Bot


class Logger:
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log = open(filename, "a", encoding="utf-8")
        self.tz = pytz.timezone("Asia/Kolkata")

    def write(self, message):
        for line in message.splitlines(True):
            if any(skip in line for skip in ["upload.GetFile"]):
                continue
            if line.strip():
                timestamp = datetime.datetime.now(self.tz).strftime("[%Y-%m-%d %H:%M:%S]")
                full_message = f"{timestamp} {line}"
            else:
                full_message = line
            self.terminal.write(full_message)
            self.log.write(full_message)

        self.flush()

    def flush(self):
        self.terminal.flush()
        self.log.flush()

sys.stdout = sys.stderr = Logger(LOG_FILE)
uvloop.install()
Bot().run()
