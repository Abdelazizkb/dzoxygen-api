
# Create your models here.

from django.db import models

# Create your models here.
from account.models import UserAccount


class Post(models.Model):
    author=models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    datetime=models.DateField(auto_now_add=True)
    size=models.IntegerField(default=0)
    price=models.BigIntegerField(default=0)
    description=models.TextField(blank=True,null=True)
    city = models.TextField(max_length=200, null=True)
    phone = models.TextField(max_length=10, null=False)



