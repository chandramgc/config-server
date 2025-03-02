import unittest
from unittest.mock import patch, MagicMock
from src.modules.config_server import ConfigServer


class TestConfigServer(unittest.TestCase):
    def setUp(self):
        # Create a ConfigServer instance with dummy values.
        self.server = ConfigServer("dummy_url", "dummy_path")
        self.client = self.server.app.test_client()

    @patch("src.modules.config_server.GitConfigManager")
    @patch("src.modules.config_server.ConfigLoader")
    def test_get_config_success(self, mock_loader_class, mock_manager_class):
        # Setup mocks to simulate a successful config load.
        mock_loader_instance = MagicMock()
        mock_loader_instance.load_config.return_value = {"config_key": "config_value"}
        mock_loader_class.return_value = mock_loader_instance

        mock_manager_instance = MagicMock()
        mock_manager_class.return_value = mock_manager_instance

        response = self.client.get("/config/dev")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"config_key": "config_value"})


if __name__ == "__main__":
    unittest.main()
