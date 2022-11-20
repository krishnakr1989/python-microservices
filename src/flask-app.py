from flask import Flask,jsonify,render_template
import socket

app = Flask(__name__)

def fetchhostDetails():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return str(hostname),str(ip_address)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/health")
def health():
    return jsonify(
        status= "200"
    ) 

@app.route('/details')
def hello():
    host,ip=fetchhostDetails()
    return render_template('index.html',HOST=host,IP=ip)

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)