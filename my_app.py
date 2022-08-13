import flask
import socket
import uuid


app=flask.Flask(__name__)
app.config["DEBUG"]=True

@app.route('/display',methods=["GET"])
def display_func():
    return f"This is a test website\nFrom socket: {socket.gethostname()}-----> \nUUID: {uuid.uuid4().hex}"


#app.run(host="0.0.0.0")

