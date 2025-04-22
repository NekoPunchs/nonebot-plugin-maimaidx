from typing import Optional, Any

from pydantic import BaseModel, Field
from util.file_util import *


class ToolsConfig(BaseModel):
    static_path: Path
    cover_path: Path
    plate_path: Path
    pic_path: Path
    rating_path: Path

    def init_path(self):
        self.cover_path = Path(self.maimaidx_path) / f"cover"
        self.plate_path = Path(self.maimaidx_path) / f"plate"
        self.pic_path = Path(self.maimaidx_path) / f"pic"
        self.rating_path = Path(self.maimaidx_path) / f"rating"


class StringID(BaseModel):
    id: int
    str: str


class MusicGroup(BaseModel):
    name: str
    music_ids: list[StringID]


class MusicData(BaseModel):
    id: int
    title: str
    type: str
    ds: list[float]
    level: list[str]
    cids: list[int]


class MusicDataContainer(BaseModel):
    json_data: list[MusicData]
    dict_data: dict[int, MusicData] = Field(default=dict[int, MusicData]())

    def __init__(self, /, **data: Any):
        super().__init__(**data)
        for md in self.json_data:
            self.dict_data[int(md.id)] = md

    def get(self, music_id: int) -> Optional[MusicData]:
        return self.dict_data.get(music_id)


def init_music_group():
    for f in get_files(Path("source/mai_configs"), ".json"):
        group = MusicGroup.model_validate_json(read_all_text(Path(f)))
        music_group[group.name] = group


tools_config = ToolsConfig.model_validate_json(read_all_text(Path("source/config.json")))
music_group = dict[str, MusicGroup]()
music_datas = MusicDataContainer.model_validate_json(read_all_text(Path("source/music_data.json")))

init_music_group()

SIYUAN: Path = tools_config.static_path / 'ResourceHanRoundedCN-Bold.ttf'
SHANGGUMONO: Path = tools_config.static_path / 'ShangguMonoSC-Regular.otf'
TBFONT: Path = tools_config.static_path / 'Torus SemiBold.otf'
