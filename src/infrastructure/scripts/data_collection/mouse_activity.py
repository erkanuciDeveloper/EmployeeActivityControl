import os
import csv
from datetime import datetime
from pynput import mouse
#from logger import logging


class MouseActivityLogger:
    # Define the log file path
    
    LOG_DIR = "./infrastructure/logs/mouse_activity_log"
    LOG_FILE = "mouse_activity_log.csv"
    HEADERS = ['timestamp', 'event', 'x', 'y', 'button', 'pressed', 'dx', 'dy']

    def __init__(self):
        self.log_file = os.path.join(self.LOG_DIR, self.LOG_FILE)
        self._ensure_log_directory()
        self._create_log_file()

    def _ensure_log_directory(self):
        os.makedirs(self.LOG_DIR, exist_ok=True)

    # Create the log file and write the headers if it doesn't exist
    def _create_log_file(self):
        if not os.path.exists(self.log_file):
            with open(self.log_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(self.HEADERS)

    def log_event(self, event_type, x, y, button=None, pressed=None, dx=None, dy=None):
        with open(self.log_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now(), event_type, x, y, button, pressed, dx, dy])
        #logging.info(f"Event logged: {event_type}, x={x}, y={y}, button={button}, pressed={pressed}, dx={dx}, dy={dy}")
    # Define the event handler fuctions
    def on_move(self, x, y):
        self.log_event('move', x, y)

    def on_click(self, x, y, button, pressed):
        self.log_event('click', x, y, button, pressed)

    def on_scroll(self, x, y, dx, dy):
        self.log_event('scroll', x, y, dx=dx, dy=dy)

    def on_double_click(self, x, y, button, pressed):
        self.log_event('double_click', x, y, button, pressed)

    def on_triple_click(self, x, y, button, pressed):
        self.log_event('triple_click', x, y, button, pressed)

    def on_right_click(self, x, y, button, pressed):
        self.log_event('right_click', x, y, button, pressed)

    def on_middle_click(self, x, y, button, pressed):
        self.log_event('middle_click', x, y, button, pressed)

    def on_drag(self, x, y, dx, dy):
        self.log_event('drag', x, y, dx=dx, dy=dy)

    def on_drop(self, x, y, dx, dy):
        self.log_event('drop', x, y, dx=dx, dy=dy)

    def on_enter(self, x, y):
        self.log_event('enter', x, y)

    def on_leave(self, x, y):
        self.log_event('leave', x, y)

    def on_hover(self, x, y):
        self.log_event('hover', x, y)

    def on_context_menu(self, x, y, button, pressed):
        self.log_event('context_menu', x, y, button, pressed)


    
    # Set up the mouse listener
    def start_logging(self):
        with mouse.Listener(
                on_move=self.on_move,
                on_click=self.on_click,
                on_scroll=self.on_scroll,
                on_double_click=self.on_double_click,
                on_triple_click=self.on_triple_click,
                on_right_click=self.on_right_click,
                on_middle_click=self.on_middle_click,
                on_drag=self.on_drag,
                on_drop=self.on_drop,
                on_enter=self.on_enter,
                on_leave=self.on_leave,
                on_hover=self.on_hover,
                on_context_menu=self.on_context_menu) as listener:
            listener.join()

if __name__ == "__main__":
    logger = MouseActivityLogger()
    logger.start_logging()
