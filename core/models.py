from django.db import models

class Gn_user(models.Model):
    userid = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    mail = models.CharField(max_length=64)
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=64)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Gn_admin(models.Model):
    adminid = models.AutoField(primary_key=True) 
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=64)

    def __str__(self):
        return self.username

class Gn_universite(models.Model):
    uni_id = models.AutoField(primary_key=True)
    uni_name = models.CharField(max_length=100)
    uni_city = models.CharField(max_length=100)
    uni_logo = models.ImageField(upload_to='uni_logo/', blank=True, null=True)

    def __str__(self):
        return self.uni_name

class Gn_Fakulte(models.Model):
    fakulte_id = models.AutoField(primary_key=True)
    fakulte_name = models.CharField(max_length=64)
    fakulte_uni = models.ForeignKey(Gn_universite, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.fakulte_uni.uni_name} - {self.fakulte_name}"

class Gn_Bolum(models.Model):
    bolum_id = models.AutoField(primary_key=True)
    bolum_name = models.CharField(max_length=100)
    bolum_fakulte = models.ForeignKey(Gn_Fakulte, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.bolum_fakulte.fakulte_uni.uni_name} - {self.bolum_fakulte.fakulte_name} - {self.bolum_name}"


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    bolum = models.ForeignKey(Gn_Bolum, on_delete=models.CASCADE)
    description = models.TextField()
    video = models.FileField(upload_to='videos/', blank=True, null=True)  # Yeni alan

    def __str__(self):
        return self.name
