from datetime import datetime
import bitbucket, settings
import dateutil.parser

client = bitbucket.Bitbucket(settings.username, settings.password)


def get_commits_stat(delta):
    repos = client.get_repos(settings.team)
    now = datetime.now()
    result = {}

    for repo in repos:
        update_date = dateutil.parser.parse(repo['updated_on']).replace(tzinfo=None)

        if update_date >= now - delta:
            commits = client.get_repo_commits(settings.team, repo)

            for commit in commits:
                commit_date = dateutil.parser.parse(commit['date']).replace(tzinfo=None)

                if commit_date >= now - delta:
                    user = commit['author']['raw']

                    if user in settings.author_rewrite:
                        user = settings.author_rewrite[user]

                    if not user in result:
                        result[user] = {'commits': 0, 'added': 0, 'removed': 0}

                    for stat in client.get_commit_diffstat(settings.team, repo, commit):
                        if stat['diffstat']['added']:
                            result[user]['added'] += stat['diffstat']['added']

                        if stat['diffstat']['removed']:
                            result[user]['removed'] += stat['diffstat']['removed']

                    result[user]['commits'] += 1

    return result
