from datetime import timedelta
from bottle import Bottle, static_file
import model

app = application = Bottle()

@app.route('/', method=['GET'])
def static_index(path='index.html'):
    return static_file(path, root='./public')


@app.route('/assets/<path:path>')
def static_assets(path):
    return static_file(path, root='./public/assets')


@app.route('/data/commits/week.json')
def data_month():
    delta = timedelta(weeks=1)
    return model.get_commits_stat(delta)


@app.route('/data/commits/month.json')
def data_month():
    delta = timedelta(weeks=4)
    return model.get_commits_stat(delta)


@app.route('/data/commits/year.json')
def data_year():
    delta = timedelta(weeks=4*12)
    return model.get_commits_stat(delta)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
