from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('create', views.create, name='create'),
    path('roomdetail<int:abc>', views.roomdetail, name='roomdetail'),
    path('comment',views.comment, name='comment'),
]
