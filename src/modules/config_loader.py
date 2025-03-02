import os
import yaml

class ConfigLoader:
    """Handles loading configuration files from the repository."""

    def __init__(self, repo_path):
        self.repo_path = repo_path

    def load_config(self, profile):
        """Loads the configuration from `application.yaml` in the specified branch."""
        config_path = os.path.join(self.repo_path, profile, "application.yaml")

        if not os.path.exists(config_path):
            return {"error": f"Configuration file not found for profile: {profile}"}

        try:
            with open(config_path, "r") as file:
                return yaml.safe_load(file)
        except yaml.YAMLError:
            return {"error": "Invalid YAML format"}
