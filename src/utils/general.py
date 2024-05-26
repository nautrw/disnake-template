import json
import os
import sys


def load_configuration():
    """Loads the bot's configuration from src/core/config.json."""
    if os.path.isfile("src/core/config.json"):
        return json.load(open("src/core/config.json"))
    else:
        sys.exit("src/core/config.json not found.")
