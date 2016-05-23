from django.conf.urls import url
from . import views
from django.contrib.auth.views import login
urlpatterns=[
    url(r'^$',views.chat,name='chat'),
    url(r'^login/',login,name='login'),
    url(r'^logout/',views.logout,name='logout'),
    
]
