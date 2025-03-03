"""
Module: config_loader
This module contains the ConfigLoader class that reads configuration files
from a cloned Git repository.
"""

import os
import yaml
import logging

# Retrieve a logger for this module.
logger = logging.getLogger(__name__)

class ConfigLoader:
    """
    Handles loading configuration files from the repository.

    Attributes:
        repo_path (str): The local path of the cloned repository.
    """

    def __init__(self, repo_path):
        """
        Initializes the ConfigLoader with the repository path.

        Args:
            repo_path (str): The path where the repository is located.
        """
        self.repo_path = repo_path

    def load_config(self, profile, application="application"):
        """
        Loads the configuration from an 'application.yaml' file in the specified branch.

        Args:
            profile (str): The branch (profile) name where the configuration file is located.

        Returns:
            dict: The configuration data if loaded successfully, or an error message.
        """
        config_path = os.path.join(self.repo_path, f"{application}.yaml")

        if not os.path.exists(config_path):
            return {"error": f"Configuration file not found for profile: {profile}"}
        try:
            with open(config_path, "r") as file:
                return yaml.safe_load(file)
        except yaml.YAMLError:
            return {"error": "Invalid YAML format"}
