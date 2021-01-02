import view as view
from django.shortcuts import render

import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from restapp.models import Employee
from restapp.serializers import EmployeeSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator



@method_decorator(csrf_exempt,name='dispatch')
class EmployeeCRUDCBV(view):
    def get(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        id=pdata.get('id',None)
        if id is not None:
            emp = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(emp)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        qs = Employee.objects.all()
        serializer = EmployeeSerializer(qs,many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
    def post(self,request,*args,**kwargs):
        json_data=request.body
        stream = io.BytesIO(json_data)
        pdata= JSONParser().parse(stream)
        serializer= EmployeeSerializer(data=pdata)
        if serializer.is_valid():
            serializer.save()
            msg ={'msg':'resources created successfully'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json',status=400)
    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id')
        emp = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(emp,data=pdata)
      #  serializer = EmployeeSerializer(emp, data=pdata,partial=True) for making partial change in table
        if serializer.is_valid():
            serializer.save()
            msg = {'msg': 'resources updated successfully'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json', status=400)
    def delete(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id')
        emp = Employee.objects.get(id=id)
        emp.delete()
        msg = {'msg': 'resource delete successfully'}
        json_data = JSONRenderer().render(msg)
        return HttpResponse(json_data, content_type='application/json')








