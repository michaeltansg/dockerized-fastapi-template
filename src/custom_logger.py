""" Custom Logger module """
# pylint: disable=too-few-public-methods
import logging
import os


class CustomLogger:
    """Custom logger class"""

    log_level = logging.INFO
    file_log_level = logging.WARNING

    @classmethod
    def setup_logger(cls, logger_name, log_file=None):
        """
        Examples:

        from src.custom_logger import CustomLogger

        logger = CustomLogger.setup_logger(__name__)
        logger.info('This is an info message')
        logger.warning('This is a warning message')
        logger.error('This is an error message')
        logger.critical('This is critical')

        For logging to a file:
        logger = CustomLogger.setup_logger(__name__, 'file.log')

        Note: All log files would be created inside the `logs` sub-folder.

        """

        # Create a custom logger
        logger = logging.getLogger(logger_name)
        logger.setLevel(cls.log_level)

        # Create console handler
        c_handler = logging.StreamHandler()
        c_handler.setLevel(cls.log_level)
        c_format = logging.Formatter("[%(levelname)s][%(name)s] %(message)s")
        c_handler.setFormatter(c_format)
        logger.addHandler(c_handler)

        # If a log file is specified, add a file handler
        if log_file is not None:
            folder_path = "logs"

            # Make directory if it doesn't exist
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            log_file = os.path.join(folder_path, log_file)

            f_handler = logging.FileHandler(log_file)
            f_handler.setLevel(cls.file_log_level)
            f_format = logging.Formatter(
                "%(asctime)s [%(levelname)s][%(name)s] %(message)s"
            )
            f_handler.setFormatter(f_format)
            logger.addHandler(f_handler)

        return logger
