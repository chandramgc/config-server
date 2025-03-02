import os
import yaml

class ConfigReader:
    """Loads application settings from YAML configuration files."""

    def __init__(self, env="dev"):
        self.config_file = f"src/config/application-{env}.yml"
        self.config = self._load_config()

    def _load_config(self):
        """Loads the YAML configuration file."""
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"Config file {self.config_file} not found!")

        with open(self.config_file, "r") as file:
            return yaml.safe_load(file)

    def get(self, key, default=None):
        """Fetch a nested configuration value."""
        keys = key.split(".")
        value = self.config
        for k in keys:
            value = value.get(k, {})
        return value or default
