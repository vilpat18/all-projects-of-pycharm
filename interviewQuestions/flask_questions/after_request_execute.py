from flask import Flask, Response

app = Flask(__name__)


@app.route('/')
def main_function():
    app.logger.info('main funct executes')
    return 'hiii vilas'


@app.after_request
def after_request():
    app.logger.info('after request')
    return Response

if __name__=='__main__':
    app.run(debug=True,port=5005)
