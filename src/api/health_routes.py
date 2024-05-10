# pylint: disable=all
from fastapi import APIRouter, Request
from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime, timezone
from tags import Tags

health_router = APIRouter(tags=[Tags.HEALTH])

class HealthCheckResponse(BaseModel):
    correlation_id: UUID = Field(
        description="The correlation id of the request.",
    )
    now: int = Field(
        description="The Unix epoch is the number of seconds that have elapsed since January 1, 1970 (midnight UTC/GMT).",
    )

@health_router.get(
    "/",
    response_model=HealthCheckResponse,
    status_code=200,
    summary="Health Check",
    description="Health check endpoint that returns the current time in milliseconds since January 1, 1970 (midnight UTC/GMT).",
)
async def get_health(request: Request) -> HealthCheckResponse:
    ms = int((datetime.now(timezone.utc) - datetime(1970, 1, 1, tzinfo=timezone.utc)).total_seconds() * 1000)
    res = HealthCheckResponse(correlation_id=UUID(request.state.correlation_id), now=ms)
    return res
