"""
Module: main
This is the entry point of the application. It loads the environment configuration,
initializes the ConfigServer, and starts the Flask API server.
"""

from src.modules.config_server import ConfigServer
from src.utils.config_reader import ConfigReader


def main():
    """
    Main function to load configuration and start the server.
    """
    # Load configuration from YAML for the 'dev' environment.
    config = ConfigReader(env="dev")  # Change to "prod" for production

    # Extract values from the configuration.
    repo_url = config.get("git.repo_url")
    local_repo_path = config.get("git.local_repo_path")
    host = config.get("server.host")
    port = config.get("server.port")

    # Start the configuration server.
    server = ConfigServer(repo_url, local_repo_path)
    server.run(host=host, port=port)


if __name__ == "__main__":
    main()
