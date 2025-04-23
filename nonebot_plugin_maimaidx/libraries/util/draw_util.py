from ..image import *
from typing import Tuple
from PIL import ImageDraw, Image


def draw_text_center(drawText: DrawText, text: str, size: int, xy: Tuple[int, int]):
    box = drawText.get_box(text, size)
    x = -(box[2] / 2) + box[0] + xy[0]
    y = -(box[3] / 2) + box[1] + xy[1] - 3
    drawText.draw(int(x), int(y), size, text)


def draw_img_center(draw: Image.Image, img: Image.Image, xy: Tuple[int, int]):
    x = xy[0] - img.size[0] / 2
    y = xy[1] - img.size[1] / 2
    draw.alpha_composite(img, (int(x), int(y)))
