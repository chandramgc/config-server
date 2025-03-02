from src.modules.config_server import ConfigServer
from src.utils.config_reader import ConfigReader

# Load configuration from YAML
config = ConfigReader(env="dev")  # Change to "prod" for production

# Extract values from YAML
repo_url = config.get("git.repo_url")
local_repo_path = config.get("git.local_repo_path")
host = config.get("server.host")
port = config.get("server.port")

# Start the server
server = ConfigServer(repo_url, local_repo_path)
server.run(host=host, port=port)
