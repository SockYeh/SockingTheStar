from fastapi import Request
from fastapi.responses import JSONResponse


class APIKeyException(Exception):
    """Raised when an invalid API key is provided"""

    pass


async def api_key_exception_handler(request: Request, exc: APIKeyException):
    return JSONResponse(
        status_code=401,
        content={"message": str(exc)},
    )
