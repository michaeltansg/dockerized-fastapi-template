""" Main module - Entry point """

import logging
# import debugpy
# debugpy.listen(("0.0.0.0", 5678))
# print("Waiting for client to attach...")
# debugpy.wait_for_client()

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from custom_logger import CustomLogger

# from load_dotenv import API_KEY
from tags import Tags
from core.middleware.cors import add_cors_middleware
from api.health_routes import health_router

CustomLogger.log_level = logging.WARNING # Set the level for logging. Default is logging.INFO

logger = CustomLogger.setup_logger(__name__)
# logger = CustomLogger.setup_logger(__name__, 'file.log')
# logger.info('This is an info message')
# logger.warning('This is a warning message')
# logger.error('This is an error message')
# logger.critical('This is critical')

tags_metadata = [
    {"name": Tags.HEALTH.value, "description": "Health check"},
]

app = FastAPI(root_path="/api", openapi_tags=tags_metadata)

# Register middleware
add_cors_middleware(app)

# Add Routers
app.include_router(health_router, prefix="/health")

@app.exception_handler(HTTPException)
async def http_exception_handler(_, exc):
    """
    This exception handler is called when a HTTPException occurs.
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """
    This exception handler is called when a request validation error occurs.
    """
    exc_str = f"{exc}".replace("\n", " ").replace("   ", " ")
    logger.error("%s: %s", request, exc_str)
    content = {"status_code": 10422, "message": exc_str, "data": None}
    logger.error("Received request: %s", request)
    return JSONResponse(
        content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
    )

@app.get("/")
async def root():
    """Root endpoint"""
    return {"Hello": "World"}
