from github.client import GitHubClient
from repo.parser import RepoParser
from repo.reports_generator import ReportsGenerator

if __name__ == '__main__':
    username = 'RamonBecker'
    response = GitHubClient.get_repos_by_user(username)

    if response['status_code'] == 200:
        repos = RepoParser.parse(response['body'])
        markdown_report = ReportsGenerator.build("MARKDOWN", repos)
        html_report = ReportsGenerator.build("HTML", repos)

        print(html_report)
        print(markdown_report)
    else:
        print(response['body'])
