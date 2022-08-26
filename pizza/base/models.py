from wsgiref.validate import validator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from django.utils.deconstruct import deconstructible


def foto_validator(image):
    image_width, image_height = get_image_dimensions(image)
    valid_width, valid_height = 706, 645
    if image_width < valid_width * 0.8 or image_width > valid_width * 1.2 or  image_height < valid_height * 0.8 or image_height > valid_height * 1.2:
        raise ValidationError('Fotoğrafın boyutları {} x {} olmalıdır. Boyutlar maksimum %20 +/- değişebilir.'.format(valid_width,valid_height))


def background_validator(image):
    image_width, image_height = get_image_dimensions(image)
    valid_width, valid_height = 1920, 850
    if image_width < valid_width * 0.7 or image_width > valid_width * 1.3 or  image_height < valid_height * 0.7 or image_height > valid_height * 1.3:
        raise ValidationError('Fotoğrafın boyutları {} x {} olmalıdır. Boyutlar maksimum %20 +/- değişebilir.'.format(valid_width,valid_height))


def logo_validator(image):
    image_width, image_height = get_image_dimensions(image)
    valid_height = 1799
    valid_width = 3673
    if image_width < valid_width * 0.8 or image_width > valid_width * 1.2 or  image_height < valid_height * 0.8 or image_height > valid_height * 1.2:
        raise ValidationError('Fotoğrafın boyutları {} x {} olmalıdır. Boyutlar maksimum %20 +/- değişebilir.'.format(valid_width,valid_height))

def galeri_validator(image):
    image_width, image_height = get_image_dimensions(image)
    if image_width != 1080 and image_height != 1080:
        raise ValidationError('Fotoğrafın boyutları {} x {} olmalıdır.'.format(1080,1080))


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
    fotograf = models.ImageField(null = True , blank = True, validators = [foto_validator])
    baslik = models.CharField(max_length= 100, null = True,blank = True)
    yazi = models.TextField(max_length= 1000, null = True,blank = True)
    arkaplan = models.ImageField(null = True,blank = True, validators = [background_validator])
    logo = models.ImageField(null = True,blank = True, validators = [logo_validator])

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
    fotograf =  models.ImageField(null = False, validators = [galeri_validator])

    def fotograf_tag(self):
        return "/images/%s" % (self.fotograf)

    def __str__(self):
        return self.isim
    

class MailAdresi(models.Model):
    class Meta:  
        verbose_name_plural = 'Mail Adresi'
    
    adres = models.CharField(max_length=100)
    def __str__(self):
        return self.adres