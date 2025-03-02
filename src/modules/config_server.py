from flask import Flask, jsonify
from src.modules.config_manager import GitConfigManager
from src.modules.config_loader import ConfigLoader

class ConfigServer:
    """REST API Server to serve configurations."""

    def __init__(self, repo_url, local_path):
        self.config_manager = GitConfigManager(repo_url, local_path)
        self.config_loader = ConfigLoader(local_path)
        self.app = Flask(__name__)
        self._setup_routes()

    def _setup_routes(self):
        """Sets up API endpoints."""
        @self.app.route('/config/<profile>', methods=['GET'])
        def get_config(profile):
            self.config_manager.update_repo(profile)
            config_data = self.config_loader.load_config(profile)

            if "error" in config_data:
                return jsonify(config_data), 404
            return jsonify(config_data)

    def run(self, host="0.0.0.0", port=5000):
        """Runs the Flask server."""
        self.app.run(host=host, port=port)
