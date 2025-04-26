plan_maps = {
    '极': '極',
}

version_maps = {
    '华': '華'
}

sdgb_plate_maps = {
    '熊': '熊&華',
    '華': '熊&華',
    '爽': '爽&煌',
    '煌': '爽&煌',
    '宙': '宙&星',
    '星': '宙&星',
    '祭': '祭&祝',
    '祝': '祭&祝',
    '双': '双&宴',
    '宴': '双&宴'
}


def plate_plan_conv(plan: str) -> str:
    result = plan_maps.get(plan)
    if result is not None:
        return result
    return plan


def plate_version_conv(version: str) -> str:
    result = version_maps.get(version)
    if result is not None:
        return result
    return version


def sdgb_plate_conv(version: str) -> str:
    result = sdgb_plate_maps.get(version)
    if result is not None:
        return result
    return version
