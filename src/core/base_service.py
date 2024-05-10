from abc import ABC, abstractmethod
from typing import Dict
from requests import Response
from fastapi import Request

class BaseService(ABC):
    def __init__(self, service_name: str, url: str, request: Request) -> None:
        self.service_name = service_name
        self.url = url
        self.correlation_id = request.state.correlation_id

    @abstractmethod
    def _request(self, headers: Dict, **kwargs) -> Response:
        pass
