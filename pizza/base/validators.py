from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions

def foto_restriction(isim):
    valid_width, valid_height = None,None
    if isim == "Anasayfa":
        valid_height, valid_width =  800,614
    elif isim == "Hikayemiz":
        valid_height, valid_width = 800,614
    elif isim == "Rezervasyon":
        valid_height, valid_width =  800,614
    elif isim == "İletişim":
        valid_height, valid_width =  800,614

    def foto_validator(image):
        image_width, image_height = get_image_dimensions(image)

        if image_width < valid_width * 0.9 or image_width > valid_width * 1.1 or  image_height < valid_height * 0.9 or image_height > valid_height * 1.1:
            raise ValidationError('Fotoğrafın boyutları {} x {} olmalıdır. Boyutlar maksimum %10 +/- değişebilir.'.format(valid_height,valid_height))
    return foto_validator

def background_restriction(isim):
    valid_width, valid_height = None,None
    if isim == "Anasayfa":
        valid_height, valid_width = 1920,1042
    elif isim == "Hikayemiz":
        valid_height, valid_width = 800,614
    elif isim == "Rezervasyon":
        valid_height, valid_width = 1920,877
    elif isim == "İletişim":
        valid_height, valid_width = 798.4,480

    def background_validator(image):
        image_width, image_height = get_image_dimensions(image)

        if image_width < valid_width * 0.9 or image_width > valid_width * 1.1 or  image_height < valid_height * 0.9 or image_height > valid_height * 1.1:
            raise ValidationError('Fotoğrafın boyutları {} x {} olmalıdır. Boyutlar maksimum %10 +/- değişebilir.'.format(valid_height,valid_height))
    return background_validator

def logo_validator(image):
    image_width, image_height = get_image_dimensions(image)
    valid_height = 529
    valid_width = 259.09
    if image_width < valid_width * 0.9 or image_width > valid_width * 1.1 or  image_height < valid_height * 0.9 or image_height > valid_height * 1.1:
        raise ValidationError('Fotoğrafın boyutları {} x {} olmalıdır. Boyutlar maksimum %10 +/- değişebilir.'.format(529,259))
    return logo_validator
    
def galeri_validator(image):
    image_width, image_height = get_image_dimensions(image)

    if image_width != 1080 and image_height != 1080:
        raise ValidationError('Fotoğrafın boyutları {} x {} olmalıdır.'.format(1080,1080))