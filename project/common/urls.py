from django.urls import path
from . import views

app_name = 'common'

urlpatterns = [
    path('master',views.master,name="master"),
    path('index',views.index,name="index"),
]