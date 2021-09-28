import json
from functools import lru_cache
from keep_alive import keep_alive
template_json = {
    "token": "",
    "git_token": "",
    "servers": [857515383691149313],
    "tag_role_id": 810514056444117024,
    "mod_role_id": 810514056444117024,
    "sub_role_id": 810514056444117024,
    "korean_role": 810514056444117024,
    "russian_role": 810514056444117024,
    "german_role": 810514056444117024,
    "french_role": 810514056444117024,
    "hindi_role": 810514056444117024,
    "tester_role": 810514056444117024,
}


@lru_cache
def get_settings(key: str):
    """Get the selected key from the settings file"""
    try:
        with open("bot_settings.json", "r", encoding="UTF-8") as f:
            _json = json.load(f)
        return _json[key]
    except FileNotFoundError:
        with open("bot_settings.json", "w", encoding="UTF-8") as f:

            json.dump(template_json, f, indent=2)
        print("No bot_settings.json found. One has been created, please populate it and restart")
        exit(1)
    except KeyError:
        print(f"Incomplete bot_settings.json found,")
        print("Adding missing keys to bot_settings.json...")
        with open("bot_settings.json", "r+", encoding="UTF-8") as f:
            _json = json.load(f)
            for key in template_json.keys():
                if key not in _json.keys():
                    _json[key] = template_json[key]
                    print(f"Added {key}")
            f.truncate(0)
            f.seek(0)
            json.dump(_json, f, indent=2)
        exit(1)


def sanity_check():
    """Scrutinizing the bot settings file to ensure smooth operation

    Note: These are Scrutinizing checks, they only check that the file is "sane" nothing more"""
    print(f"Scrutinizing bot_settings.json\n{''.center(33, '=')}")
    failed = False
    for key in template_json.keys():
        data = get_settings(key)
        if data is None or data in ["Put Bot Token Here", "Put Git Token Here"]:
            failed = True
            print(f"{key} has not been set to a value")
    if failed:
        exit(1)
    print("Scrutinize checks passed\n\n")
keep_alive()