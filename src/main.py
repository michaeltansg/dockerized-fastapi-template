# import logging
# from src.custom_logger import CustomLogger
# logger = CustomLogger.setup_logger(__name__, 'file.log', level=logging.WARNING)
# logger.warning('This is a warning!')

# import debugpy
# debugpy.listen(("0.0.0.0", 5678))
# print("Waiting for client to attach...")
# debugpy.wait_for_client()

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}
