from flask import Flask

app = Flask(__name__)

@app.route('/hello/<int:age>')
def greet(age):
    return "india is awesome %d"

if __name__=="__main__":
    app.run()


