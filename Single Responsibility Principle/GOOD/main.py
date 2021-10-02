from github.client import GitHubClient
from repo.parser import RepoParser


if __name__ == '__main__':
    username = 'RamonBecker'
    response = GitHubClient.get_repos_by_user(username)

    if response['status_code'] == 200:
        RepoParser.parse(response['body'])
    else:
        print(response['body'])
