import os
from loguru import logger
from datetime import datetime


class LogManager:
    logs_dir = "logs"

    @staticmethod
    def create_log_directory():
        if not os.path.exists(LogManager.logs_dir):
            os.makedirs(LogManager.logs_dir)

    @staticmethod
    def create_log_file_name():
        return f"{LogManager.logs_dir}/log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

    @staticmethod
    def check_files_in_dir():
        log_files = [os.path.join(LogManager.logs_dir, i) for i in os.listdir(LogManager.logs_dir)
                     if i.startswith("log_") and i.endswith(".log")]
        log_files.sort(key=os.path.getctime)
        while len(log_files) > 10:
            os.remove(log_files.pop(0))

    @staticmethod
    def create_log_file():
        LogManager.create_log_directory()

        LogManager.check_files_in_dir()

        logger.add(
            LogManager.create_log_file_name(),
            format="{time} {level} {message}"
        )

    @staticmethod
    def get_logger():
        LogManager.create_log_file()
        return logger
