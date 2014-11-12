from datetime import datetime, timedelta
from bottle import Bottle, static_file
import settings, bitbucket
import dateutil.parser

client = bitbucket.Bitbucket(settings.username, settings.password)
app = Bottle()


@app.route('/', method=['GET'])
def static_index(path='index.html'):
    return static_file(path, root='./public')


@app.route('/assets/<path:path>')
def static_assets(path):
    return static_file(path, root='./public/assets')


@app.route('/data/week.json')
def data_month():
    delta = timedelta(weeks=1)
    return get_data(delta)


@app.route('/data/month.json')
def data_month():
    delta = timedelta(weeks=4)
    return get_data(delta)


@app.route('/data/half-year.json')
def data_year():
    delta = timedelta(weeks=4*6)
    return get_data(delta)


def get_data(delta):
    repos = client.get_repos(settings.team)
    now = datetime.now()
    result = {}

    for repo in repos:
        update_date = dateutil.parser.parse(repo['updated_on']).replace(tzinfo=None)

        if update_date >= now - delta:
            commits = client.get_repo_commits(settings.team, repo['name'])

            for commit in commits:
                commit_date = dateutil.parser.parse(commit['date']).replace(tzinfo=None)

                if commit_date >= now - delta:
                    user = commit['author']['raw']

                    if user in settings.author_rewrite:
                        user = settings.author_rewrite[user]

                    if not user in result:
                        result[user] = {'commits': 0, 'added': 0, 'removed': 0}

                    for stat in client.get_commit_diffstat(settings.team, repo['name'], commit['hash']):
                        if stat['diffstat']['added']:
                            result[user]['added'] += stat['diffstat']['added']

                        if stat['diffstat']['removed']:
                            result[user]['removed'] += stat['diffstat']['removed']

                    result[user]['commits'] += 1

    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
