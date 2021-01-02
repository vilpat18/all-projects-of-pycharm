from flask import Flask

app = Flask(__name__)


@app.route('/fetch')
def fetch():
    return "hello world"

app.run(debug=True)