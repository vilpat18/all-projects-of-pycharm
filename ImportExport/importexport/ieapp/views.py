from django.shortcuts import render

# Create your views here.
from .resources import PersonResources
from django.http import HttpResponse
from rest_framework.decorators import api_view
from tablib import Dataset
from rest_framework.response import Response




# def export(request):
#     person_resources = PersonResources()
#     dataset = person_resources.export()
#     response = HttpResponse(dataset.csv, content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="person.csv"'
#     return response

# @api_view(['POST'])
# def export_data(request):
#     if request.method == "POST":
#         file_format = request.POST['file-format']
#         person_resources = PersonResources()
#         dataset = person_resources.export()
#         if file_format == 'CSV':
#             response = HttpResponse(dataset.csv,content_type='text/csv')
#             response['Content-Disposition'] = 'attachment; filename="person.csv"'
#             return response
#     return render(request,'export.html')




