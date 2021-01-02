from flask import Blueprint

mod = Blueprint("calculator",__name__,url_prefix='/math')

@mod.route('/',methods=['GET'])
def all():
    return "1.addition \n 2.substraction"

@mod.route('<id>/<num1>/<num2>',methods=["GET"])
def math_operations(id,num1,num2):
    if id=='1':
        n1=int(num1)
        n2=int(num2)
        s=n1+n2
        ss=str(s)
        return ss
    elif  id=='2':
        n1=int(num1)
        n2=int(num2)
        s=n1-n2
        ss=str(s)
        return ss