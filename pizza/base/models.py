from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import mark_safe
# Create your models here.
class User(AbstractUser):
    class Meta:  
        verbose_name_plural = 'Kullanıcılar'
    email = models.EmailField(unique=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']



class Sayfa(models.Model):
    class Meta:  
        verbose_name_plural = 'Sayfalar'

    isim = models.CharField(max_length=50,unique=True)
    fotograf = models.ImageField(null = True , blank = True)
    baslik = models.CharField(max_length= 100, null = True,blank = True)
    yazi = models.TextField(max_length= 1000, null = True,blank = True)
    arkaplan = models.ImageField(null = True,blank = True)
    logo = models.ImageField(null = True,blank = True)

    def fotograf_tag(self):
        return "/images/%s" % (self.fotograf)
    def arkaplan_tag(self):
        return "/images/%s" % (self.arkaplan)
    def logo_tag(self):
        return "/images/%s" % (self.logo)


    def __str__(self):
        return self.isim

class Menu(models.Model):
    class Meta:  
        verbose_name_plural = 'Menü'
    isim = models.CharField(max_length=50, unique=True)
    menu = models.FileField()

    def menu_tag(self):
        return "/images/%s" % (self.menu)
    

    def __str__(self):
        return self.isim

class GaleriFoto(models.Model):
    class Meta:  
        verbose_name_plural = 'Galeri Fotoğrafları'
    isim = models.CharField(max_length=50)
    fotograf =  models.ImageField(null = False)

    def fotograf_tag(self):
        return "/images/%s" % (self.fotograf)

    def __str__(self):
        return self.isim
    
