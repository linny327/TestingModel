from django.contrib import admin
from django.urls import path, include
#from . import views
#from rest_framework import routers


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('prediction.urls')),
    path('', include('vitalsigns.urls'))
    #path('api/', prediction.site.urls),

]
