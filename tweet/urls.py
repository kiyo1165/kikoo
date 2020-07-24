from django.urls import path
from . import views

appname = 'tweet'

urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
]
