from flask import Blueprint

mod = Blueprint("calculator",__name__,url_prefix='/math')

@mod.route('/',methods=['get'])
def all():
    return "1.addition \n 2.subtraction"

@mod.route("<id>/<n1>/<n2>",methods=['GET'])
def math_operations(id,n1,n2):
      if id=='1':
        num1=int(n1)
        num2=int(n2)
        s=num1+num2
        ss=str(s)
        return ss

      elif id=='2':
        num1 = int(n1)
        num2 = int(n2)
        s = num1 - num2
        ss = str(s)
        return ss