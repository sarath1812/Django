from django.contrib import admin
from django.urls import path
#from django.conf.urls import re_path as path,include
from django.conf.urls import re_path as path , include

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('',include('cms.urls'))
]

# Contain all the url declerations needed for this project.
