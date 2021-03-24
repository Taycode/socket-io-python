"""Flask APP"""

from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/socket')
def index():
	"""index page"""
	return render_template('index.html')


@app.route('/send')
def send_message():
	"""Sends message"""
	socketio.send('hello')
	return {'sent': 'yes'}


@socketio.on('message')
def handle_message(data):
	"""Handle Messages Flask"""
	print('received message: ', data)


@socketio.on('json')
def handle_json(data):
	"""Handle JSON"""
	print('received json', str(data))


@socketio.on('my event')
def handle_my_custom_event(data):
	"""Handles Custom event"""
	print('received json:', str(data))


if __name__ == '__main__':
	socketio.run(app)
