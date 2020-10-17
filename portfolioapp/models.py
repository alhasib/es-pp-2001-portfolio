from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 250)
    photo = models.ImageField()
    address = models.CharField(max_length = 250, blank = True, null = True)
    fb_id = models.CharField(max_length = 250, blank=True, null=True)
    linkedin_id = models.CharField(max_length = 250, blank=True, null=True)

    def __str__(self):
        return str(self.user)

class AboutMe(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about_me = models.TextField(max_length = 500)

    def __str__(self):
        return str(self.user)


class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 250)

    def __str__(self):
        return str(self.user)

class Interest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 250)

    def __str__(self):
        return str(self.user)


class Award(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 250)

    def __str__(self):
        return str(self.user)

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name_of_institution = models.CharField(max_length = 250)
    passing_year = models.DateField()
    department = models.CharField(max_length = 250)
    name_of_degree = models.CharField(max_length = 250)

    def __str__(self):
        return str(self.user)

class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name_of_company = models.CharField(max_length = 250)
    start_date = models.DateField()
    end_date = models.DateField()
    designation = models.CharField(max_length = 250)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.user)
