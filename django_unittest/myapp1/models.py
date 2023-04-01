from django.db import models

class MyApp1(models.Model):
    SEX_CHOICES = (("male", "Male"), ("female", "Female"), ("other", "Other"))
    name = models.CharField('Name', max_length = 200)
    surname = models.CharField('Surname', max_length = 200)
    age = models.CharField('Age', max_length = 200)
    status = models.BooleanField('Status', default=True)
    sex = models.CharField(max_length=20, choices=SEX_CHOICES, default='Nothing choosed')

    def __str__(self):
        return self.name + " " + self.surname
        
class Meta:
    verbose_name = 'user'
    verbose_name_plural = 'users'

from django.db import models

class MyApp2(models.Model):
    SEX_CHOICES = (("male", "Male"), ("female", "Female"), ("other", "Other"))
    name = models.CharField('Name', max_length = 200)
    surname = models.CharField('Surname', max_length = 200)
    age = models.CharField('Age', max_length = 200)
    status = models.BooleanField('Status', default=True)
    sex = models.CharField(max_length=20, choices=SEX_CHOICES, default='Nothing choosed')

    def __str__(self):
        return self.name + " " + self.surname
        
class Meta:
    verbose_name = 'user'
    verbose_name_plural = 'users'

from django.db import models

class MyApp3(models.Model):
    SEX_CHOICES = (("male", "Male"), ("female", "Female"), ("other", "Other"))
    name = models.CharField('Name', max_length = 200)
    surname = models.CharField('Surname', max_length = 200)
    age = models.CharField('Age', max_length = 200)
    status = models.BooleanField('Status', default=True)
    sex = models.CharField(max_length=20, choices=SEX_CHOICES, default='Nothing choosed')

    def __str__(self):
        return self.name + " " + self.surname
        
class Meta:
    verbose_name = 'user'
    verbose_name_plural = 'users'
