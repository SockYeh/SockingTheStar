from fastapi import APIRouter, Request
from fastapi.responses import FileResponse
from utils.ratelimit_handler import limiter
from utils.image_handler import random_picture
import io

router = APIRouter(prefix="/api/animals", tags=["animals"])


@router.get("/dog")
@limiter.limit("30/minute")
async def dog(request: Request):
    img = random_picture("dog")
    return FileResponse(img)


@router.get("/cat")
@limiter.limit("30/minute")
async def cat(request: Request):
    img = random_picture("cat")
    return FileResponse(img)


@router.get("/koala")
@limiter.limit("30/minute")
async def koala(request: Request):
    img = random_picture("koala")
    return FileResponse(img)


@router.get("/fox")
@limiter.limit("30/minute")
async def fox(request: Request):
    img = random_picture("red_fox")
    return FileResponse(img)
