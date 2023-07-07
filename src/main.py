""" Main module - Entry point """

# import logging
# from src.custom_logger import CustomLogger
#
# CustomLogger.log_level = logging.WARNING # Set the level for logging. Default is logging.INFO
#
# logger = CustomLogger.setup_logger(__name__)
# logger = CustomLogger.setup_logger(__name__, 'file.log')
# logger.info('This is an info message')
# logger.warning('This is a warning message')
# logger.error('This is an error message')
# logger.critical('This is critical')

# import debugpy
# debugpy.listen(("0.0.0.0", 5678))
# print("Waiting for client to attach...")
# debugpy.wait_for_client()

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    """Root endpoint"""
    return {"Hello": "World"}
