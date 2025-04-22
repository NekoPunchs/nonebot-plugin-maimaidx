from pathlib import Path
from typing import Tuple, Union

from PIL import ImageFont, ImageDraw


class DrawText:

    def __init__(self, image: ImageDraw.ImageDraw, font: Path) -> None:
        self._img = image
        self._font = str(font)

    def get_box(self, text: str, size: int) -> Tuple[float, float, float, float]:
        return ImageFont.truetype(self._font, size).getbbox(text)

    def draw(
            self,
            pos_x: int,
            pos_y: int,
            size: int,
            text: Union[str, int, float],
            color: Tuple[int, int, int, int] = (255, 255, 255, 255),
            anchor: str = 'lt',
            stroke_width: int = 0,
            stroke_fill: Tuple[int, int, int, int] = (0, 0, 0, 0),
            multiline: bool = False
    ) -> None:
        font = ImageFont.truetype(self._font, size)
        if multiline:
            self._img.multiline_text(
                (pos_x, pos_y),
                str(text),
                color,
                font,
                anchor,
                stroke_width=stroke_width,
                stroke_fill=stroke_fill
            )
        else:
            self._img.text(
                (pos_x, pos_y),
                str(text),
                color,
                font,
                anchor,
                stroke_width=stroke_width,
                stroke_fill=stroke_fill
            )
