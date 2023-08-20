
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def carousel():
    return render_template('app.html')

@app.route('/static/<path:filename>')
def send_static(filename):
    return send_from_directory('static', filename)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5001, debug=True)