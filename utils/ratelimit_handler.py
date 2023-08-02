from fastapi import Request
from .database_handler import validate_api_key
from .general_exceptions import APIKeyException
from slowapi import Limiter


def get_api_key(request: Request) -> str:
    """Returns the api key for the current request"""
    if "Authorization" not in request.headers:
        raise APIKeyException("No API key provided")
    if validate_api_key(request.headers["Authorization"]):
        return request.headers["Authorization"]


limiter = Limiter(key_func=get_api_key, default_limits=["30/minute"])
