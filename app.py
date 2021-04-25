from flask import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        x = request.environ['REMOTE_ADDR']
    else:
        x = request.environ['HTTP_X_FORWARDED_FOR']
    picture = 'https://www.gravatar.com/avatar/ebab91cbcb3b97466e70e58dcd4cb020?s=256'
    return render_template('index.html',ip=x,picture=picture)



if __name__ == '__main__':
    app.run()
