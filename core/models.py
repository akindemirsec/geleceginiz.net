from django.db import models

class Gn_user(models.Model):
    userid = models.AutoField(primary_key=True)  # Otomatik artan bir alan olarak tanımla
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    mail = models.CharField(max_length=64)
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=64)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

class Gn_admin(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=64)
