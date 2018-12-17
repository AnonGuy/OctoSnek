"""Query methods for getting repositories from GitHub."""

from typing import List

import requests


endpoint = 'https://api.github.com/search/repositories'


def get_repos(query: str, limit: int) -> List[dict]:
    """Return a JSON object of repos from a query."""
    repos: List[dict] = []
    results = requests.get(
        endpoint, params={'q': query, 'sort': 'stars'}
    ).json()['items']
    for count, repo in enumerate(results, 1):
        repos.append(
            dict(
                number=count,
                name=repo.get('full_name'),
                url=repo.get('clone_url')
            )
        )
    return repos


def display_repos(repos: List[dict]) -> None:
    """Take a list of repos and pretty print them."""
    for repo in repos:
        print(
            repo['number'],
            '\033[4m%s\033[0m' % repo['name']
        )
        print(repo.get('url'), end='\n\n')


def install_repo(repo_object: dict) -> None:
    """Take a repo as a dict and intelligently install."""
    ...
