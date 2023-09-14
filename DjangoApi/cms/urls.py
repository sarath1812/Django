#from django.urls import   re_path as path
from django.urls import path

from . import views

urlpatterns=[
    #re_path(r'^department$',views.departmentApi)
    path('',views.testData,name = 'test'),
    path('json/',views.jsonData,name = 'test')

]



