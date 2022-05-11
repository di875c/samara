from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', csrf_exempt(views.MainPage.as_view())),
    path('error/', csrf_exempt(views.ErrorView.as_view())),
    path('aboutus/', csrf_exempt(views.AboutUs.as_view())),
    path('resume', RedirectView.as_view(url='aboutus')),
]