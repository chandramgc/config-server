"""
Module: config_server
This module implements the ConfigServer class which creates a Flask API server
to serve configuration data fetched from a Git repository.
"""

from flask import Flask, jsonify, request
from src.modules.config_manager import GitConfigManager
from src.modules.config_loader import ConfigLoader
import logging

# Retrieve a logger for this module.
logger = logging.getLogger(__name__)

class ConfigServer:
    """
    REST API Server to serve configurations.

    Attributes:
        config_manager (GitConfigManager): Instance to manage Git operations.
        config_loader (ConfigLoader): Instance to load configuration files.
        app (Flask): The Flask application instance.
    """

    def __init__(self, repo_url, local_path):
        """
        Initializes the ConfigServer with the Git repository details.

        Args:
            repo_url (str): The URL of the Git repository.
            local_path (str): The local directory path for the repository.
        """
        self.config_manager = GitConfigManager(repo_url, local_path)
        self.config_loader = ConfigLoader(local_path)
        self.app = Flask(__name__)
        self._setup_routes()

    def _setup_routes(self):
        """
        Sets up the API endpoints for the Flask application.
        """

        @self.app.route("/config/<profile>", methods=["GET"])
        def get_config(profile):
            """
            Endpoint to get configuration for a specified profile.

            Args:
                profile (str): The branch (profile) for which to load the configuration.

            Returns:
                Response: A JSON response containing the configuration or an error.
            """
            app_name = request.args.get("app", "application")
            logger.info(f"Fetching configuration for profile: {profile}, app: {app_name}")
            self.config_manager.update_repo(profile)
            config_data = self.config_loader.load_config(profile, app_name)

            if "error" in config_data:
                return jsonify(config_data), 404
            return jsonify(config_data)

    def run(self, host="0.0.0.0", port=5000):
        """
        Runs the Flask server.

        Args:
            host (str, optional): The host IP. Defaults to "0.0.0.0".
            port (int, optional): The port number. Defaults to 5000.
        """
        self.app.run(host=host, port=port)
