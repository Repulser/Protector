import json
from datetime import datetime


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


def clean_message(content: str) -> str:
    """
    Cleans message content.
    :param content: Content to clean
    :return: Clean content
    """
    return content.replace("`", "")


def get_time_string():
    return datetime.utcnow().strftime("%H:%M:%S")
