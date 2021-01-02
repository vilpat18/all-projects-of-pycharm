from flask import Flask

app = Flask(__name__)

@app.before_first_request
def before_first_request():
    app.logger.info('before_first_request')

@app.route('/')
def main_func():
    app.logger.info('main_function')
    return 'hello world'


if __name__=='__main__':
    app.run(debug=True,port=5000)