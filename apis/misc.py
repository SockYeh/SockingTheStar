from fastapi import APIRouter

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


@router.post("/emorse")
async def emorse(query: str):
    emorsed = ""
    for char in query:
        if char != " ":
            emorsed += MORSE_CODE_DICT[char] + " "
        else:
            emorsed += " "

    return emorsed


@router.post("/demorse")
async def demorse(query: str):
    query += " "

    demorsed = ""
    cit = ""

    for char in query:
        if char != " ":
            i = 0
            cit += char
        else:
            i += 1
            if i == 2:
                demorsed += " "
            else:
                demorsed += list(MORSE_CODE_DICT.keys())[
                    list(MORSE_CODE_DICT.values()).index(cit)
                ]

    return demorsed


@router.post("/ebinary")
async def ebinary(query: str):
    ebinaried = " ".join(format(ord(x), "b") for x in query)
    return ebinaried


@router.post("/ebinary")
async def debinary(query: str):
    return debinaried
