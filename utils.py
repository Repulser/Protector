import json


def load_config() -> dict:
    """
    Loads json config.
    :return: Loaded config or None if not found
    """
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
            return config
    except FileNotFoundError:
        print("Config file not found, make sure config.json is present in working dir.")
