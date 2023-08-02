from utils.ratelimit_handler import limiter
from fastapi import APIRouter, File, Request, Form
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
from image_modifiers.twitter import twitter
from image_modifiers.youtube import youtube
import io

router = APIRouter(prefix="/api/frame", tags=["frame"])


@router.post("/yt")
@limiter.limit("30/minute")
async def yt(
    request: Request,
    pfp: bytes = File(...),
    username: str = Form(...),
    comment: str = Form(...),
):
    img = youtube(
        pfp_bytes=pfp,
        name=username,
        text=comment,
    )
    img_path = io.BytesIO()
    img.save(img_path, format="PNG")
    img_path.seek(0)
    return StreamingResponse(img_path, media_type="image/png")


@router.post("/tweet")
@limiter.limit("30/minute")
async def yt(
    request: Request,
    pfp: bytes = File(...),
    username: str = Form(...),
    displayname: str = Form(...),
    comment: str = Form(...),
    is_verified: bool = Form(False),
):
    img = twitter(
        pfp_bytes=pfp,
        username=username,
        displayname=displayname,
        text=comment,
        is_verified=is_verified,
    )
    img_path = io.BytesIO()
    img.save(img_path, format="PNG")
    img_path.seek(0)
    return StreamingResponse(img_path, media_type="image/png")
