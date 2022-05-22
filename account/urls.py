from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from . import views


url_pattern = [
    path('', csrf_exempt(views.AccountView.as_view())),
]