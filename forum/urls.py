from django.conf.urls import  url
from . import views


app_name ='forum'
urlpatterns = (


    url(r'^posts/$', views.posts, name='posts'),
    url(r'^(?P<answer_id>[\d+])/like/$',views.upvoteAnswerToggle,name="like-toggle")
)
