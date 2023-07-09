""" Main module - Entry point """

# import logging
# from custom_logger import CustomLogger
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
# from load_dotenv import API_KEY

app = FastAPI()


@app.get("/")
async def root():
    """Root endpoint"""
    return {"Hello": "World"}
