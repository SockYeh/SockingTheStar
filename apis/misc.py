from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse
from utils.ratelimit_handler import limiter
import base64, json


MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
}

router = APIRouter(prefix="/api/misc", tags=["misc"])

# from main import limiter


@router.get("/emorse")
@limiter.limit("30/minute")
async def emorse(request: Request, query: str):
    try:
        morse = "".join([MORSE_CODE_DICT[i.upper()] + " " for i in query])
        return JSONResponse(content={"output": morse}, status_code=status.HTTP_200_OK)
    except KeyError:
        return JSONResponse(
            content={"output": "Invalid input."}, status_code=status.HTTP_404_NOT_FOUND
        )


@router.get("/demorse")
@limiter.limit("30/minute")
async def demorse(request: Request, query: str):
    try:
        reved_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
        demorse = "".join([reved_dict[i] for i in query.split()])
        return JSONResponse(content={"output": demorse}, status_code=status.HTTP_200_OK)
    except KeyError:
        return JSONResponse(
            content={"output": "Invalid input."}, status_code=status.HTTP_404_NOT_FOUND
        )


@router.get("/ebinary")
@limiter.limit("30/minute")
async def ebinary(request: Request, query: str):
    try:
        ebinaried = " ".join(format(ord(x), "b") for x in query)
        return JSONResponse(
            content={"output": ebinaried}, status_code=status.HTTP_200_OK
        )
    except TypeError:
        return JSONResponse(
            content={"output": "Invalid input."}, status_code=status.HTTP_404_NOT_FOUND
        )


@router.get("/debinary")
@limiter.limit("30/minute")
async def debinary(request: Request, query: str):
    try:
        debinaried = "".join(chr(int(x, 2)) for x in query.split())
        return JSONResponse(
            content={"output": debinaried}, status_code=status.HTTP_200_OK
        )
    except TypeError:
        return JSONResponse(
            content={"output": "Invalid input."}, status_code=status.HTTP_404_NOT_FOUND
        )


@router.get("/b64encode")
@limiter.limit("30/minute")
async def b64encode(request: Request, query: str):
    try:
        b64encoded = base64.b64encode(query.encode("ascii")).decode("ascii")
        return JSONResponse(
            content={"output": b64encoded}, status_code=status.HTTP_200_OK
        )
    except TypeError:
        return JSONResponse(
            content={"output": "Invalid input."}, status_code=status.HTTP_404_NOT_FOUND
        )


@router.get("/b64decode")
@limiter.limit("30/minute")
async def b64decode(request: Request, query: str):
    try:
        b64decoded = base64.b64decode(query.encode("ascii")).decode("ascii")
        return JSONResponse(
            content={"output": b64decoded}, status_code=status.HTTP_200_OK
        )
    except TypeError:
        return JSONResponse(
            content={"output": "Invalid input."}, status_code=status.HTTP_404_NOT_FOUND
        )


@router.get("/dictionary")
@limiter.limit("30/minute")
async def dictionary(request: Request, query: str):
    with open("data/dictionary.json", "r") as f:
        dictionary = json.load(f)
    try:
        return JSONResponse(
            content={"word": query, "definitions": dictionary[query.lower()]},
            status_code=status.HTTP_200_OK,
        )
    except KeyError:
        return JSONResponse(
            content={"output": "Word not found."}, status_code=status.HTTP_404_NOT_FOUND
        )
