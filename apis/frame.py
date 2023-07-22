from PIL import Image, ImageDraw, ImageFont
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/frame", tags=["frame"])


class Youtube(BaseModel):
    username: str
    comment: str


class Tweet(BaseModel):
    pass


class PH(BaseModel):
    pass


@router.post("/yt")
async def yt(data: Youtube):
    return {"omk"}
