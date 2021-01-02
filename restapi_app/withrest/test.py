import requests
import json

BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/'


'''def get_resoursec(id=None):
    data = {}
    if id is not None:
        data = {
            'id':id
        }
    resp = requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())

get_resoursec(1)'''

'''def create_resourse():
    new_emp = {
        'eno' : '100',
        'ename': 'dhoni',
        'esal':'1000',
        'eadd':'ranchi'
     }
    r = requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
    print(r.status_code)
    print(r.json())

create_resourse()'''

'''def update_resource(id):
    new_data = {
        'id':'id',
        'ename': 'ajay',
    'esal':'2000'
    }
    r = requests.post(BASE_URL + ENDPOINT, data=json.dumps(new_data))
    print(r.status_code)
    print(r.json())
update_resource(2)'''



def delete_resource(id=None):
        data = {
            'id':id
         }
        resp = requests.delete(BASE_URL+ENDPOINT,data=json.dumps(data))
        print(resp.status_code)
        print(resp.json())

delete_resource(1)


'''def post(self,request):
        serializer = NameSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            name = serializer.data.get('name')
            msg = name
            return Response({'msg':msg})
        else:
            return Response(serializer.errors,status=400)'''


