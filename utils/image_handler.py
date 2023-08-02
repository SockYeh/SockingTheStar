from PIL import Image, ImageDraw, ImageOps
import io, random, os


def circle_pfp(pfp_bytes: bytes, size: int) -> Image:
    pfp = Image.open(io.BytesIO(pfp_bytes))
    pfp = ImageOps.fit(pfp, (size, size), Image.LANCZOS)
    mask = Image.new("L", pfp.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + pfp.size, fill=255)
    pfp.putalpha(mask)
    return pfp


def random_picture(name: str) -> os.path:
    imgs = os.listdir(f"data\{name}")
    return os.path.join(f"data\{name}", random.choice(imgs))


# import re

# text = "YouTubeAmazingPlace"

# print(re.split(r"(?=[A-Z])", text))
