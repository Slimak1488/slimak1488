
from flask import Flask, render_template, request, url_for, redirect, send_from_directory,jsonify
from werkzeug.utils import secure_filename
from flask_socketio import SocketIO, emit

import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/', methods=['GET'])
def clock():
   return render_template('clock.html')


#@app.route("/time", methods=['GET'])
#def get_time():
#    return jsonify(datetime.datetime.now().strftime('%H'), datetime.datetime.now().strftime('%M'))


@socketio.on('connect')
def mes():
    time_h = datetime.datetime.now().strftime('%H')
    time_m = datetime.datetime.now().strftime('%M')
    print("OK")
    return emit('time',{'min': time_m,'hour': time_h})




#@socketio.on('message')

if __name__ == '__main__':
    socketio.run(app)