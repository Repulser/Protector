import json
from datetime import datetime
import string

printable = set(string.printable)


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
    return content.replace("`", "").replace("*", "").replace("_", "")


def ascii_filter(content: str) -> str:
    """
    Strips message from ascii.
    :param content: Content to strip
    :return: Stripped content
    """
    return ''.join(filter(lambda x: x in printable, content))


def get_time_string():
    return datetime.utcnow().strftime("%H:%M:%S")
