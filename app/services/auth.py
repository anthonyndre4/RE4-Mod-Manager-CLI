from typing import Any
from pydantic import BaseModel
from pydantic_settings import BaseSettings
import requests

from app.exceptions.auth import BaseClientException, NexusAuthException

DATA_REQUESTS = ["PATCH", "POST", "PUT"]

HTTP_REQUESTS = ["GET", "DELETE"] + DATA_REQUESTS


class BaseNexusClient(BaseSettings):
    accountId: str

    @property
    def headers(self) -> dict[str, str]:
        return {"apikey": self.accountId}

    @property
    def base_url(self) -> str:
        return "https://api.nexusmods.com"

    def base_request(self, **kwargs) -> Any:
        """This is the base request function for the 'BaseNexusClient' class.
        It takes the following parameters.
        1. Request Type (request_type) - get, delete, post etc
        2. Model (model) - (Optional) What pydantic model it will be converting the response into.
        3. URL (url) - What url will be amended onto the base url.
        4. Data (data) - (Optional) What data will be sent into the payload of the request.

        Returns:
            The given pydantic model in a array or a single model or a integer (status code).
        """
        request_type = kwargs.get("request_type")
        model: BaseModel | None = kwargs.get("model")
        url = kwargs.get("url")
        data = kwargs.get("data")
        if not request_type:
            raise BaseClientException(HTTP_REQUESTS)
        if kwargs.get("data"):
            request = requests.request(
                request_type,
                f"{self.base_url}{url}",
                data=data,
                headers=self.headers,
            )
        else:
            request = requests.request(
                request_type, f"{self.base_url}{url}", headers=self.headers
            )
        if not request.ok:
            raise NexusAuthException(request)
        if kwargs.get("is_list") and model:
            responses: list[Any] = []
            for response in request.json():
                responses.append(model.model_validate(response))
            return responses
        s_code = request.status_code
        return model.model_validate(request.json()) if model else s_code

    def get(self, url: str, model: Any) -> Any:
        """This function is a standard HTTP 'GET' Request utilising the 'do' method.
        Parameters:
        1. URL (url) - What url will be amended onto the base url.
        2. Model (model) - (Optional) What pydantic model it will be converting the response into.
        Returns:
            The given pydantic model.
        """
        return self.base_request(request_type="get", model=model, url=url)

    def delete(self, url: str) -> Any:
        """This function is a standard HTTP 'DELETE' Request utilising the 'base_request' method.
        Parameters:
        1. URL (url) - What url will be amended onto the base url.
        Returns:
            The status code returned from the request.
        """
        return self.base_request(request_type="delete", url=url)

    def post(self, url: str, model: Any, data: Any | None = None) -> Any:
        """This function is a standard HTTP 'POST' Request utilising the 'base_request' method.
        Parameters:
        1. URL (url) - What url will be amended onto the base url.
        2. Model (model) - (Optional) What pydantic model it will be converting the response into.
        3. Data (data) - (Optional) What data will be sent into the payload of the request.
        Returns:
            The given pydantic model.
        """
        return self.base_request(request_type="post", model=model, url=url, data=data)

    def patch(self, url: str, model: Any, data: Any) -> Any:
        """This function is a standard HTTP 'PATCH' Request utilising the 'base_request' method.
        Parameters:
        1. URL (url) - What url will be amended onto the base url.
        2. Model (model) - (Optional) What pydantic model it will be converting the response into.
        3. Data (data) - (Optional) What data will be sent into the payload of the request.
        Returns:
            The given pydantic model.
        """
        return self.base_request(request_type="patch", model=model, url=url, data=data)

    def list(self, url: str, model: Any) -> Any:
        """This function is a standard HTTP 'PATCH' Request utilising the 'do' method.
        Parameters:
        1. URL (url) - What url will be amended onto the base url.
        2. Model (model) - (Optional) What pydantic model it will be converting the response into.
        Returns:
            A list of the given pydantic model.
        """
        return self.base_request(request_type="get", model=model, url=url, is_list=True)
