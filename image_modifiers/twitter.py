from utils.image_handler import circle_pfp
from PIL import Image, ImageDraw, ImageFont, ImageOps
from random import choices
from string import ascii_lowercase
from textwrap import wrap
import warnings


warnings.filterwarnings("ignore", category=DeprecationWarning)


def twitter(pfp_bytes, username, displayname, text, is_verified):
    if len(text) > 280:
        return None
    ntext = "\n".join(wrap(text, 100))
    bg_color = Image.open(r"image_modifiers\pillow_data\twitter_data\twitter_bg.jpg")
    d1 = ImageDraw.Draw(bg_color)

    username_font = ImageFont.truetype(
        r"image_modifiers\pillow_data\twitter_data\fonts\Black.ttf",
        size=30,
    )

    display_font = ImageFont.truetype(
        r"image_modifiers\pillow_data\twitter_data\fonts\Regular.ttf",
        size=30,
    )

    comment_font = ImageFont.truetype(
        r"image_modifiers\pillow_data\twitter_data\fonts\Bold.ttf",
        size=30,
    )

    _, height = d1.multiline_textsize(ntext, comment_font, spacing=10)

    pfp = circle_pfp(pfp_bytes, 90)

    rsize_height = height + 150 + 300 + 20

    bg_color = bg_color.resize((1260, rsize_height))
    d1 = ImageDraw.Draw(bg_color)
    d1.text(
        (10, 140),
        f"{ntext.lstrip()}",
        spacing=10,
        fill=(216, 216, 216),
        font=comment_font,
    )
    d1.text((125, 20), f"{displayname}", fill=(216, 216, 216), font=username_font)
    flen = int(d1.textlength(f"{displayname}", username_font))

    d1.text((126, 60), f"@{username}", fill=(127, 127, 137), font=display_font)

    bg_color.paste(pfp, (10, 8), pfp)

    likes_img = Image.open(
        r"image_modifiers\pillow_data\twitter_data\twitter_likes.jpg"
    )
    _, lheight = likes_img.size

    bg_color.paste(likes_img, (0, rsize_height - lheight - 10))

    if is_verified:
        verified_img = Image.open(
            r"image_modifiers\pillow_data\twitter_data\twitter_verified.jpg"
        )
        bg_color.paste(verified_img, (130 + flen + 5, 20))

    return bg_color
