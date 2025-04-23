plan_maps = {
    "极": "極",
}


def plate_plan_conv(plan: str) -> str:
    result = plan_maps.get(plan)
    if result is not None:
        return result
    return plan
