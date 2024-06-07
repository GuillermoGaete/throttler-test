from github import Auth
from github import Github
import os 
class GithubData:
    def __init__(self, repo, access_token) -> None:
        auth = Auth.Token(access_token)
        self.github = Github(auth=auth)
        self.repo = self.github.get_repo(repo)

    def get_pr_diff(self, pr_number):
        pr = self.repo.get_pull(pr_number)
        return [
            {
                "filename": file.filename,
                "patch": file.patch
            }
            for file in pr.get_files()
        ]

    def get_pr_commit_messages(self, pr_number):
        pr = self.repo.get_pull(pr_number)
        commits = pr.get_commits()

        return list(map(lambda commit: commit.commit.message, commits))

if __name__ == "__main__":
    githubData = GithubData(os.getenv('REPO_PATH'), os.getenv('GITHUB_ACTIONS_TOKEN'))
    pr_diff = githubData.get_pr_diff(1)
    print(pr_diff)