from flask import Flask, render_template, request, session
from flask_socketio import SocketIO, join_room, leave_room, emit
from flask_cors import CORS
from flask_session import Session

import random
import string

app = Flask(__name__)
app.debug = True
app.config['SECRET_TYPE'] = 'secret!'
app.config['SESSION_TYPE'] = 'filesystem'

Session(app)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins = '*')

def randomText():
    chars = "".join([random.choice(string.ascii_letters) for i in range(12)])
    return chars

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat',methods = ['GET', 'POST'])
def chat():
    if(request.method == 'GET'):
        socketio.emit('message',randomText())
        return 'BOS'
    else: 
        return 'AA'
 
@socketio.on('connect')
def welcome():
  print('Welcome Socket')


if __name__ == "__main__":
    socketio.run(app)

