from django.db import models
from django.contrib.auth.models import User

STATUS = (
(0,"Draft"),
(1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length = 200, unique=True)
    