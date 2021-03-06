import json
from pathlib import Path


def extract_profile(profile=""):
    home = Path.home()
    config_dir = home / ".aliyun"
    config_file = config_dir / "config.json"
    with config_file.open() as f:
        config = f.read()

    config = json.loads(config)
    found = list(filter(lambda p: p["name"] == profile, config["profiles"]))
    if len(found) > 0:
        return found[0]
    else:
        return None


def extract_credentials(profile_obj):
    if "access_key_id" not in profile_obj or "access_key_secret" not in profile_obj:
        raise Exception(
            "Invalid Alibaba Cloud credentials loaded, missing access key ID or access key secret"
        )

    return (
        profile_obj["access_key_id"],
        profile_obj["access_key_secret"],
        profile_obj["region_id"],
    )
