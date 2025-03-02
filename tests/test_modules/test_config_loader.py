import os
import tempfile
import unittest
import yaml
from src.modules.config_loader import ConfigLoader


class TestConfigLoader(unittest.TestCase):
    def test_load_config_success(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            profile = "dev"
            os.makedirs(os.path.join(temp_dir, profile))
            config_file = os.path.join(temp_dir, profile, "application.yaml")
            sample_data = {"key": "value"}
            with open(config_file, "w") as f:
                yaml.dump(sample_data, f)
            loader = ConfigLoader(temp_dir)
            loaded_config = loader.load_config(profile)
            self.assertEqual(loaded_config, sample_data)

    def test_load_config_missing_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            profile = "nonexistent"
            loader = ConfigLoader(temp_dir)
            loaded_config = loader.load_config(profile)
            self.assertIn("error", loaded_config)


if __name__ == "__main__":
    unittest.main()
