"""
Module: config_manager
This module contains the GitConfigManager class that handles fetching and updating
the configuration from a Git repository.
"""

import os
import git


class GitConfigManager:
    """
    Manages fetching and updating configuration from a Git repository.

    Attributes:
        repo_url (str): The URL of the Git repository.
        local_path (str): The local path where the repository is cloned.
        repo (git.Repo): The Git repository object.
    """

    def __init__(self, repo_url, local_path):
        """
        Initializes the GitConfigManager with the repository URL and local path.

        Args:
            repo_url (str): URL of the Git repository.
            local_path (str): Local directory path to clone or access the repository.
        """
        self.repo_url = repo_url
        self.local_path = local_path
        self.repo = None
        self._initialize_repo()

    def _initialize_repo(self):
        """
        Clones the Git repository if it does not exist locally; otherwise, initializes it.

        Raises:
            Exception: If cloning or initializing the repository fails.
        """
        if os.path.exists(self.local_path):
            self.repo = git.Repo(self.local_path)
        else:
            self.repo = git.Repo.clone_from(self.repo_url, self.local_path)

    def update_repo(self, profile):
        """
        Updates the repository by checking out the branch corresponding to the given profile
        and pulling the latest changes.

        Args:
            profile (str): The branch (profile) to update and check out.

        Returns:
            dict: An error dictionary if the update fails; otherwise, None.
        """
        try:
            self.repo.git.fetch()
            if profile in self.repo.branches:
                self.repo.git.checkout(profile)
            else:
                self.repo.git.checkout("-b", profile, f"origin/{profile}")
            self.repo.remotes.origin.pull()
        except Exception as e:
            return {"error": f"Failed to update repo: {str(e)}"}
