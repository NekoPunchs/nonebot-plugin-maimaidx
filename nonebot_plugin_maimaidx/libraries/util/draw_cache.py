from PIL import Image
from ...config import *
from ..maimaidx_model import PlayInfoDefault
from ..maimaidx_best_50 import computeRa

cache_icons = dict[str, Image.Image]()


def get_complete_icon(play: PlayInfoDefault, is_rate: bool) -> Image.Image:
    if is_rate:
        rate = computeRa(play.ds, play.achievements, onlyrate=True)
        result = cache_icons.get(rate)
        if result is None:
            result = Image.open(maimaidir / f'UI_TTR_Rank_{rate}.png').resize((102, 46))
            cache_icons[rate] = result
    else:
        fc = fcl[play.fc]
        result = cache_icons.get(fc)
        if result is None:
            result = Image.open(maimaidir / f'UI_CHR_PlayBonus_{fc}.png').resize((75, 75))
            cache_icons[fc] = result
    return result
