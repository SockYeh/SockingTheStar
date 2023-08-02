from fastapi import FastAPI
import os
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from utils.ratelimit_handler import get_api_key, limiter
from utils.general_exceptions import APIKeyException, api_key_exception_handler
from apis import animals, auth, misc, anime, frame, filters
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

app = FastAPI()
routers = [
    animals.router,
    auth.router,
    misc.router,
    anime.router,
    frame.router,
    filters.router,
]
for router in routers:
    app.include_router(router)


app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_exception_handler(APIKeyException, api_key_exception_handler)

if __name__ == "__main__":
    os.system("uvicorn main:app --reload")
