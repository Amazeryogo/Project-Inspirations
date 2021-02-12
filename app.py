from flask import Flask,render_template,request,redirect
from hashlib import md5

app = Flask(__name__)


@app.route('/')
def hello_world():
    ip_address = request.remote_addr
    picture = 'https://www.gravatar.com/avatar/' + md5(b'suvid.datta@gmail.com').hexdigest() + '?s=256'
    return render_template('index.html',ip=ip_address,picture=picture)

# THESE ARE EASTER EGGS, DONT TAKE THEM SERIOUSLY
@app.route('/discord-nitro')
def nitro():
    return redirect("https://project-inspirations.herokuapp.com/nevergonnagiveyouup")

@app.route('/nevergonnagiveyouup')
def lol():
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

if __name__ == '__main__':
    app.run()
