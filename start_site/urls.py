from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from . import views
from account.views import account_view, tlgrm_id_nfound
from django.views.generic import RedirectView

urlpatterns = [
    path('', csrf_exempt(views.MainPage.as_view())),
    path('error/', csrf_exempt(views.ErrorView.as_view())),
    path('aboutus/', csrf_exempt(views.AboutUs.as_view())),
    path('resume/', RedirectView.as_view(url='aboutus')),
    path('account/', csrf_exempt(account_view), name='project-view'),
    path('account/id-not-found', csrf_exempt(tlgrm_id_nfound)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', csrf_exempt(views.SignView.as_view()), name='sign-view'),
    path('accounts/update/', csrf_exempt(views.user_change_settings), name='update-view'),
]