import json
import os


def load_configuration(config_directory: str):
    """Loads the bot's configuration from src/core/config.json."""
    return json.load(open(config_directory)) # Json already handles errors