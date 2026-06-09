import os
from datetime import datetime
from git import Repo, InvalidGitRepositoryError


def load_repo(path):
    try:
        repo = Repo(path)
        return repo
    except InvalidGitRepositoryError:
        raise ValueError(f"no git repo found at {path}")


def get_commits(repo):
    commits = []
    for commit in repo.iter_commits():
        commits.append({
            "hash": commit.hexsha[:8],
            "author": commit.author.email,
            "timestamp": datetime.fromtimestamp(commit.authored_date),
            "message": commit.message.strip(),
            "files_changed": list(commit.stats.files.keys()),
            "insertions": commit.stats.total["insertions"],
            "deletions": commit.stats.total["deletions"],
        })
    return commits


def get_file_owners(commits):
    # count how many commits each dev has touched each file
    ownership = {}  # file -> {email: count}
    for commit in commits:
        author = commit["author"]
        for f in commit["files_changed"]:
            if f not in ownership:
                ownership[f] = {}
            ownership[f][author] = ownership[f].get(author, 0) + 1
    return ownership


def get_dev_list(commits):
    devs = set()
    for c in commits:
        devs.add(c["author"])
    return list(devs)


def get_commits_by_dev(commits):
    by_dev = {}
    for c in commits:
        author = c["author"]
        if author not in by_dev:
            by_dev[author] = []
        by_dev[author].append(c)
    return by_dev


def parse_repo(path):
    repo = load_repo(path)
    commits = get_commits(repo)

    if not commits:
        raise ValueError("repo has no commits")

    return {
        "commits": commits,
        "file_owners": get_file_owners(commits),
        "devs": get_dev_list(commits),
        "by_dev": get_commits_by_dev(commits),
        "repo_name": os.path.basename(os.path.abspath(path)),
    }