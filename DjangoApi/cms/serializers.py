from rest_framework import serializers
from cms.models import Department

class DepartmentSerializer(serializers.ModelSerializer): 
    class Meta : 
        model = Department
        fields=('DepId','DepName')

