from django.db import models


class Saves(models.Model):
    image = models.ImageField(upload_to='main/static/user_img/')
    done_img = models.ImageField(upload_to='main/static/done_img/')
    from_user = models.TextField()
    to_user = models.TextField()
