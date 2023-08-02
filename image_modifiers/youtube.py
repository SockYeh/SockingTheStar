from PIL import Image, ImageDraw, ImageFont
from random import choices
from string import ascii_lowercase
from textwrap import wrap
from utils.image_handler import circle_pfp
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)


def youtube(pfp_bytes, name, text):
    ntext = "\n".join(wrap(text, 55))
    bg_color = Image.open(
        r"image_modifiers\pillow_data\youtube_data\empty_yutube_bg.png"
    )
    d1 = ImageDraw.Draw(bg_color)

    username_font = ImageFont.truetype(
        r"image_modifiers\pillow_data\youtube_data\fonts\Bold.ttf",
        size=21,
    )

    time_font = ImageFont.truetype(
        r"image_modifiers\pillow_data\youtube_data\fonts\Light.ttf",
        size=19,
    )

    comment_font = ImageFont.truetype(
        r"image_modifiers\pillow_data\youtube_data\fonts\Regular.ttf",
        size=22,
    )

    _, height = d1.multiline_textsize(ntext, comment_font, spacing=10)

    pfp = circle_pfp(pfp_bytes, 86)

    _, imgheight = pfp.size

    rsize_height = height + imgheight + 45 + 10

    bg_color = bg_color.resize((750, rsize_height))
    d1 = ImageDraw.Draw(bg_color)
    d1.text(
        (113, 60),
        f"{ntext.lstrip()}",
        spacing=10,
        fill=(241, 241, 241),
        font=comment_font,
    )
    d1.text((113, 20), f"@{name}", fill=(241, 241, 241), font=username_font)
    flen = d1.textlength(f"@{name}", username_font)
    d1.text(
        (113 + flen + 10, 22),
        f"7 months ago",
        fill=(168, 168, 168),
        font=time_font,
    )

    bg_color.paste(pfp, (10, 10), pfp)

    likes_img = Image.open(
        r"image_modifiers\pillow_data\youtube_data\empty_yutube_likes.png"
    )
    lkd = ImageDraw.Draw(likes_img)
    _, lheight = likes_img.size
    # lkd.text((40, 10), likes, fill=(165, 165, 165), font=time_font)

    bg_color.paste(likes_img, (115, rsize_height - lheight - 10))

    return bg_color
