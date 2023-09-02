from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    tg_id = models.BigIntegerField()  # telegram id is id for models
    tg_username = models.CharField(max_length=64, null=True, blank=True)
    tg_language_code = models.CharField(max_length=16,
                                        default='en')  # could be with dialects

    def __str__(self):
        return f'{self.first_name} {self.last_name}(@{self.username})'
