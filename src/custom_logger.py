''' Custom Logger module '''
# pylint: disable=too-few-public-methods
import logging
import os

class CustomLogger:
    ''' Custom logger class '''

    @classmethod
    def setup_logger(cls, logger_name, log_file=None, level=logging.INFO):
        '''
        Examples:
        import logging
        from src.custom_logger import CustomLogger

        logger = CustomLogger.setup_logger(__name__, level=logging.WARNING)
        logger = CustomLogger.setup_logger(__name__, 'file.log', level=logging.WARNING)

        logger.warning('This is a warning message')
        logger.error('This is an error message')

        Note: All log files would be created inside the `logs` sub-folder.
        '''

        # Create a custom logger
        logger = logging.getLogger(logger_name)
        logger.setLevel(level)

        # Create console handler
        c_handler = logging.StreamHandler()
        c_handler.setLevel(level)
        c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        c_handler.setFormatter(c_format)
        logger.addHandler(c_handler)

        # If a log file is specified, add a file handler
        if log_file is not None:
            folder_path='logs'

            # Make directory if it doesn't exist
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            log_file = os.path.join(folder_path, log_file)

            f_handler = logging.FileHandler(log_file)
            f_handler.setLevel(level)
            f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            f_handler.setFormatter(f_format)
            logger.addHandler(f_handler)

        return logger
