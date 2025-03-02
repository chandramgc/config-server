import unittest
from unittest.mock import patch, MagicMock
from src.modules.config_manager import GitConfigManager


class TestGitConfigManager(unittest.TestCase):
    @patch("src.modules.config_manager.os.path.exists", return_value=False)
    @patch("src.modules.config_manager.git.Repo.clone_from")
    def test_initialize_repo_clone(self, mock_clone, mock_exists):
        # When the local path does not exist, clone_from should be called.
        GitConfigManager("dummy_url", "dummy_path")
        mock_clone.assert_called_with("dummy_url", "dummy_path")

    @patch("src.modules.config_manager.os.path.exists", return_value=True)
    @patch("src.modules.config_manager.git.Repo")
    def test_initialize_repo_existing(self, mock_repo, mock_exists):
        # When the local path exists, Repo should be used to initialize the repo.
        instance = MagicMock()
        mock_repo.return_value = instance
        manager = GitConfigManager("dummy_url", "dummy_path")
        self.assertIsNotNone(manager.repo)


if __name__ == "__main__":
    unittest.main()
