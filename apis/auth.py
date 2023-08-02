from fastapi import APIRouter, Response
from pydantic import BaseModel
from utils.database_handler import create_user, validate_user, get_user_by_email
from utils.jwt_handler import signJWT

router = APIRouter(prefix="/api/auth", tags=["auth"])


class Login(BaseModel):
    email: str
    password: str


class Register(BaseModel):
    email: str
    password: str
    username: str


@router.post("/login")
async def login(response: Response, payload: Login):
    print(validate_user(payload.email, payload.password))
    if validate_user(payload.email, payload.password):
        user = get_user_by_email(payload.email)
        userid = user["id"]
        jwt_token = signJWT(userid)
        response.set_cookie(key="session", value=jwt_token["access_token"])
        return {"success": True, "message": "Logged in"}


@router.post("/register")
async def register(response: Response, payload: Register):
    if not get_user_by_email(payload.email):
        user = create_user(payload.email, payload.username, payload.password)
        userid = user["id"]
        jwt_token = signJWT(userid)
        response.set_cookie(key="session", value=jwt_token["access_token"])
        return {"success": True, "message": "User created"}
    return {"success": False, "message": "User already exists"}
