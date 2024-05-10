from uuid import UUID
from pydantic import BaseModel, Field

class HealthCheckResponse(BaseModel):
    correlation_id: UUID = Field(
        description="The correlation id of the request.",
    )
    now: int = Field(
        description="The Unix epoch is the number of seconds that have elapsed since January 1, 1970 (midnight UTC/GMT).",
    )
