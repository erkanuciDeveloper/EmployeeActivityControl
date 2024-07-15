import logging
import os
from datetime import datetime

class Logger:
    def __init__(self, log_dir="logs", log_file=None, title=None):
        self.log_dir = log_dir
        self.log_file = log_file if log_file else f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
        self.title = title
        self._create_log_directory()
        self._configure_logging()

    def _create_log_directory(self):
        os.makedirs(self.log_dir, exist_ok=True)

    def _configure_logging(self):
        log_file_path = os.path.join(self.log_dir, self.log_file)
        logging.basicConfig(
            filename=log_file_path,
            format=f"[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - {self.title or ''} - %(message)s",
            level=logging.INFO,
        )

#if __name__ == "__main__":
    #logger = Logger(log_file="my_logs.log", title="Custom Title")
