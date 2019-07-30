from django.contrib import admin
from django.urls import path , include

import app_board.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app_board.views.login, name='login'),
    path('account/',include('app_board.urls')),
    path('main/',include('loveroom.urls')),
]
