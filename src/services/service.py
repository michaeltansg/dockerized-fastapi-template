# pylint: disable=all
import requests
import json
from typing import Dict
from requests import Response
from fastapi import Request
from core.base_service import BaseService


class Service(BaseService):
    def __init__(self, url: str, request: Request) -> None:
        super().__init__("Service", url, request)

    def _request(self, headers: Dict, **kwargs) -> Response:
        data = {
            "param1": {},
            "param2": kwargs.get("arg1", "default_value")
        }
        headers["accept"] = "application/json"
        headers["content-type"] = "application/json"
        response = requests.post(self.url, headers=headers, data=json.dumps(data))

        # import curlify
        # print(curlify.to_curl(response.request))

        return response
