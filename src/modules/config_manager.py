import os
import git

class GitConfigManager:
    """Manages fetching and updating configuration from a Git repository."""

    def __init__(self, repo_url, local_path):
        self.repo_url = repo_url
        self.local_path = local_path
        self.repo = None
        self._initialize_repo()

    def _initialize_repo(self):
        """Clones or initializes the Git repository."""
        if os.path.exists(self.local_path):
            self.repo = git.Repo(self.local_path)
        else:
            self.repo = git.Repo.clone_from(self.repo_url, self.local_path)

    def update_repo(self, profile):
        """Pulls the latest configuration from a specific branch (profile)."""
        try:
            self.repo.git.fetch()
            if profile in self.repo.branches:
                self.repo.git.checkout(profile)
            else:
                self.repo.git.checkout('-b', profile, f'origin/{profile}')
            self.repo.remotes.origin.pull()
        except Exception as e:
            return {"error": f"Failed to update repo: {str(e)}"}
