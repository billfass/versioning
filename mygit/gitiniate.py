from git import Repo

class Gitinit:
    def __init__(self, repo_path, repo_url, commit_message, branch_name, username, token):
        self.repo_path = repo_path
        self.repo_url = repo_url
        self.commit_message = commit_message
        self.branch_name = branch_name
        self.username = username
        self.token = token
        self.repo = Repo.init(self.repo_path)

    def add_all_files_to_repo(self):
        self.repo.git.add(all=True)

    def perform_git_commit(self):
        self.repo.git.commit("-m", self.commit_message)

    def add_github_remote(self):
        self.repo.git.remote("add", "origin", self.repo_url)
        self.repo.git.remote("set-url", "origin", self.repo_url.replace("https://", f"https://{self.username}:{self.token}@"))

    def push_to_github(self):
        self.repo.git.push("--set-upstream", "origin", f"master:{self.branch_name}")

    def compute(self):
        self.add_all_files_to_repo()
        self.perform_git_commit()
        self.add_github_remote()
        self.push_to_github()

    