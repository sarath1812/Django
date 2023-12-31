from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# importing the above one to allow accessing of other domains to our api methods.
# Create your views here.
from rest_framework.parsers import JSONParser
# To parse the data 
from django.http.response import JsonResponse

from cms.models import Department
from cms.serializers import DepartmentSerializer

# Writing the api methods.

@csrf_exempt
def departmentApi(request , id = 0): 
    if request.method == 'GET': 
        departments = Department.objects.all()
        dep_Serializer = DepartmentSerializer(departments,many = True)
        return JsonResponse(dep_Serializer.data,safe=False)
    
def testData(request): 
    return HttpResponse('<h1>Hey Buddy this peice of code in running using the python and Django</h1>')

def jsonData(request): 

    return JsonResponse({
   "username" : "my_username",
   "password" : "my_password",
   "validation-factors" : {
      "validationFactors" : [
         {
            "name" : "remote_address",
            "value" : "127.0.0.1"
         }
      ]
   }
})