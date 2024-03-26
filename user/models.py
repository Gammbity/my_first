from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    user_img = models.ImageField(upload_to = 'user/', default='/static/img/user-icon.png')
