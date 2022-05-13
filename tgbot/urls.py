from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from samara.settings import WEBHOOK
from . import views

urlpatterns = [  
    # TODO: make webhook more secure
    path('', views.index, name="index"),
    path(f'{WEBHOOK}/', csrf_exempt(views.TelegramBotWebhookView.as_view())),
]


https://api.telegram.org/5373087878:AAGtqZAUdeFfscupY6dFoiXqe35wFbKg2q8/setWebhook?url=https://samara-business.ru/AAGtqZAUdeFfscupY6dFoiXqe35wFbKg2q8/
https://api.telegram.org/botТОКЕН/setWebhook?url=ВАША_ССЫЛКА