from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.


class User(AbstractUser):
    birthdate = models.DateField(
        verbose_name='Date of birth',
        blank=False,
        null=True
    )


class Weighing(models.Manager):
    weight = models.FloatField(
        verbose_name='Weight'
    )
    date = models.DateTimeField(
        verbose_name='Weighing date',
        auto_now_add=True
    )
    user = models.ForeignKey(
        to=get_user_model(),
        related_name='weighings',
        related_query_name='weighings',
        on_delete=models.CASCADE
    )
