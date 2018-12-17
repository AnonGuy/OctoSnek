"""Octosnek: Query, Clone and Install repositories from GitHub.

Usage:
    octo search <repo_name>
    octo clone <repo_name>
    octo auto-install <repo_name>

Options:
    -h --help       Show this screen.
    --limit=<limit> Limit of displayed repos. [default: 3]
    -v --verbose    Increase verbosity of logging messages.
    -V --version    Show version.
"""

from docopt import docopt

from .utils import display_repos, get_repos


if __name__ == '__main__':
    arguments = docopt(__doc__, version='Octosnek 1.0')
    limit = arguments.get('<limit>')
    name = arguments.get('<repo_name>')
    if arguments.get('search'):
        repos = get_repos(name, limit)
        display_repos(repos)
