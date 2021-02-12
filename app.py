from flask import Flask,render_template,request
from hashlib import md5

app = Flask(__name__)


@app.route('/')
def hello_world():
    ip_address = request.remote_addr
    picture = 'https://www.gravatar.com/avatar/' + md5(b'suvid.datta@gmail.com').hexdigest() + '?s=256'
    return render_template('index.html',ip=ip_address,picture=picture)


if __name__ == '__main__':
    app.run()
