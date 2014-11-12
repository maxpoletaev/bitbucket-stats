from filecache import filecache
import requests

CACHE_TIME = 24 * 60 * 60

class Bitbucket:
    url = 'https://bitbucket.org/api'

    def __init__(self, username, password):
        self.credentials = (username, password)

    @filecache(CACHE_TIME)
    def send_request_v1(self, uri):
        request = requests.get('%s/1.0/%s' % (self.url, uri), auth=self.credentials)
        response = request.json()

        return response

    @filecache(CACHE_TIME)
    def send_request_v2(self, uri):
        request = requests.get('%s/2.0/%s' % (self.url, uri), auth=self.credentials)

        response = request.json()
        data = response['values']

        while 'next' in response:
            request = requests.get(response['next'], auth=self.credentials)
            response = request.json()
            data.extend(response['values'])

        return data

    def get_repos(self, user):
        return self.send_request_v2('repositories/%s' % user)

    def get_repo_commits(self, user, repo):
        repo_slug = repo['name'] if isinstance(repo, dict) else repo
        return self.send_request_v2('repositories/%s/%s/commits' % (user, repo_slug.lower()))

    def get_commit_diffstat(self, user, repo, commit):
        repo_slug = repo['name'] if isinstance(repo, dict) else repo
        commit_hahs = commit['hash'] if isinstance(commit, dict) else commit

        diffstat = self.send_request_v1('repositories/%s/%s/changesets/%s/diffstat/'
            % (user, repo_slug.lower(), commit_hahs))

        return diffstat
