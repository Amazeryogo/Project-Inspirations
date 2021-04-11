from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/')
def hello_world():
    ip_address = request.remote_addr
    picture = 'https://www.gravatar.com/avatar/ebab91cbcb3b97466e70e58dcd4cb020?s=256'
    return render_template('index.html',ip=ip_address,picture=picture)



if __name__ == '__main__':
    app.run()
