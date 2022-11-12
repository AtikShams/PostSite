from django.db import models
from django.contrib.auth.models import User


class post(models.Model):
    tital = models.CharField(max_length=40)
    des = models.TextField()
    uid = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
