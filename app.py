from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def render_initial_page():
    return render_template("index.html")

@socketio.on("message")
def handle_message(message):
    emit("message", f"Client Message: {message}", broadcast=True)

if __name__ == "__main__":
    socketio.run(app, debug=True)