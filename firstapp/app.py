from flask import Flask
app = Flask(__name__)

'''@app.route('/')
def hello_world():
    return 'Hello, World!'''


#passing the arguments as admin
''''@app.route("/user/<admin>")
def classs(admin):
    return "hello whats up? "'''


#to take integer as a argument
'''@app.route("/home/<int:rnumber>")
def karthik(rnumber):
    return "the roll number is"


@app.route("/home/<float:money>")
def karla(money):
    return "the biggest in asia"

@app.route("/project/")
def project():
    return "the project page"

@app.route('/about')
def about():
    return "tell me somthing about yourself"'''

from flask import request
@app.route('/login',methods=['GET','POST'])
def long():
    if request.method == 'POST':
        return 'login'
    else:
        return 'longterm'


if __name__=="__main__":
    app.run(debug=True, port=5001)

