from requests import Response


class NexusAuthException(Exception):

    def __init__(self, response: Response) -> None:
        self.response = response

    def __str__(self) -> str:
        status_code = self.response.status_code
        return f"Error has occured [{status_code}]: {self.response.reason}"


class BaseClientException(Exception):

    def __init__(self, http_requests: list[str]) -> None:
        self.http_requests = http_requests

    def __str__(self) -> str:
        requests = self.http_requests
        err1 = "Please Include a valid HTTP request method"
        return f"{err1}. Expected {requests}."
