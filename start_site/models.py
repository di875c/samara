# from tgbot.models import User
from django.contrib.auth.models import User
from django.db import models


class MainUser(User):
    #Extension base User model by additional fields
    #Make it from Abstract User https://habr.com/ru/post/313764/?
    #or update other methods from User https://www.djbook.ru/examples/6/?
    user_tg_id = models.PositiveBigIntegerField(default=None)
    description = models.CharField(max_length=512)
