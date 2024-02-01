
import time
from datetime import datetime, timedelta

class Timer:
    def __init__(self, duration):
        self.duration = duration
        self.end_time = datetime.now() + timedelta(seconds=duration)
        self.running = False

    def start(self):
        self.running = True

    def get_remaining_time(self):
        if not self.running:
            return "00:00:00:00"
        remaining_time = self.end_time - datetime.now()
        if remaining_time.total_seconds() <= 0:
            return "00:00:00:00"
        days, remainder = divmod(remaining_time.total_seconds(), 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(days):02}:{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

    def is_finished(self):
        return datetime.now() >= self.end_time
