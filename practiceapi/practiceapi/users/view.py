from flask import Blueprint,jsonify
import json

mod = Blueprint("users",__name__,url_prefix="/users")

#read json data

#fp = open("data.json","r")
data = json.load(open("data.json","r"))

@mod.route('/',methods=['GET'])
def fetch():
    return jsonify(data)

#@mod.route('/<username>',methods =["GET"])
#def show(username):
 #   return jsonify(username)
