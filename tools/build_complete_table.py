from typing import Tuple

from tools_config import *
from PIL import Image, ImageDraw
from util import draw_text
from util import draw_util

# cache
level_bg = Image.open(Path("source/image/build_level.png"))
const_cover_size = (100, 100)
const_label_rect = (0, 80, 100, 100)
label_bg_color = (124, 129, 255)


def build_table():
    plate_path = tools_config.plate_path
    for group in music_group.values():
        build_table_impl(group, plate_path / f"{group.name}.png")


def draw_level_icon(bg: Image.Image, level: str, xy: Tuple[int, int]):
    draw = ImageDraw.Draw(bg)
    text = draw_text.DrawText(draw, SIYUAN)
    draw_util.draw_img_center(bg, level_bg, xy)
    draw_util.draw_text_center(text, level, 28, xy)


def draw_cover(bg: Image.Image, music_id: int, xy: Tuple[int, int]):
    path = tools_config.cover_path / f"{music_id}.png"
    if not os.path.exists(path):
        path = tools_config.cover_path / f"0.png"
    cover = Image.open(path).resize(const_cover_size)
    # label
    dw = ImageDraw.Draw(cover)
    dw.rectangle(const_label_rect, fill=label_bg_color)
    # txt
    text = draw_text.DrawText(dw, SIYUAN)
    x0, y0, x1, y1 = const_label_rect[0], const_label_rect[1], const_label_rect[2], const_label_rect[3]
    txt_xy = (int((x1 - x0) / 2 + x0),
              int((y1 - y0) / 2) + y0)
    draw_util.draw_text_center(text, str(music_id), 18, txt_xy)
    # bg
    cover_xy = (int(xy[0] - cover.size[0] / 2), int(xy[1] - cover.size[1] / 2))
    bg.alpha_composite(cover, cover_xy)


def level_group_by(group: MusicGroup) -> dict[str, list[MusicData]]:
    result = dict[str, list[MusicData]]()
    for music_id in group.music_ids:
        data = music_datas.get(music_id.id)
        if data is None:
            print(f"maybe deleted music.{music_id}")
            continue

        if len(data.level) == 5 and group.name != "舞":
            # exclude re:Master
            last_level = data.level[-2]
        else:
            last_level = data.level[-1]

        mds = result.get(last_level)
        if mds is None:
            mds = list[MusicData]()
            result[last_level] = mds
        mds.append(data)
    return result


def calc_col_max_count(cover_width: int, total_width: int, padding: int) -> int:
    count = 1
    while 1:
        if count * cover_width + (count - 1) * padding > total_width:
            break
        count += 1
    return count - 1


def build_table_impl(group: MusicGroup, imgPath: Path):
    bg = (Image.open(tools_config.pic_path / f"complete_table_bg.png")
          .convert("RGBA")
          .resize((1600, 2500)))  # 祭&祝最大需要2500h

    # 舞 = 1600x6550
    if group.name == "舞":
        bg = bg.resize((1600, 6550))

    begin_y = 325
    begin_x = 170
    padding = 20

    level_group = level_group_by(group)
    sorted_keys = sorted(level_group, reverse=True)

    max_cols = calc_col_max_count(const_cover_size[0], bg.size[0] - begin_x, padding)
    col = 0
    row = 0

    for key in sorted_keys:
        draw_level_icon(bg, key,
                        (begin_x - level_bg.size[0],
                         int(begin_y + row * (const_cover_size[1] + padding) + const_cover_size[1] / 2)))
        musics = level_group[key]
        for md in musics:
            x = begin_x + col * (const_cover_size[0] + padding) - padding + const_cover_size[0] / 2
            y = begin_y + row * (const_cover_size[1] + padding) + const_cover_size[1] / 2
            draw_cover(bg, md.id, (int(x), int(y)))
            col += 1
            if col >= max_cols:
                col = 0
                row += 1
        if col != 0:
            row += 1
            col = 0
    bg.save(imgPath, format="png")
    # bg.show("preview")
