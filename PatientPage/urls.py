from django.conf.urls import  url
from . import views


app_name ='PatientPage'
urlpatterns = (


    url(r'^(?P<Patient_name>[\w-]+)$', views.index, name='index'),
    url(r'^(?P<Patient_name>[\w-]+)/changeDP/', views.changeProfilePic, name='changeProfilePic'),

)
