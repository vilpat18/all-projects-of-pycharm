from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.

def json_view(request):
    my_dict = {
        'e_no':100,
        'e_name': 'viru',
        'e_sal': 1000,
        'e_add':'london'
    }
    json_data = json.dumps(my_dict)
    return HttpResponse(json_data,content_type='application/json')
