from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Todo(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    name = models.CharField(max_length=250, blank=False, null=False)
    image = models.ImageField(blank=False, null=False) # use base64 upload
    deadline = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
