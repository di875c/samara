from django.db import models
from utils.models import CreateTracker, GetOrNoneManager
from tgbot.models import User


class AccountModel(CreateTracker):
    objects = GetOrNoneManager()
    user = models.ForeignKey(User,
                             related_name = 'items',
                             on_delete = models.CASCADE)
    project_name = models.CharField(max_length=32, blank = True)
    bill_link = models.URLField(blank=True, null=True) #ссылка на ОФД
    bill_photo = models.ImageField(upload_to='start_site/static/', null=True, blank=True) # photo or link?
    sum_value = models.FloatField(default=0.0)
