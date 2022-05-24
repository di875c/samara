# from tgbot.models import User
from django.contrib.auth.models import User
from django.db import models


class MainUser(User):
    #Extension base User model by additional fields
    #or update other methods from User https://www.djbook.ru/examples/6/?
    user_tg_id = models.PositiveBigIntegerField(null=True, blank=True)
    description = models.CharField(max_length=512)
