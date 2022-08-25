from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import GaleriFoto, Menu, User, Sayfa

class CustomUserAdmin(UserAdmin):
    model = User


admin.site.register(User)
admin.site.register(Sayfa)
admin.site.register(GaleriFoto)
admin.site.register(Menu)

fields = ['fotograf_tag', 'arkaplan_tag', 'logo_tag']
readonly_fields = ['fotograf_tag', 'arkaplan_tag', 'logo_tag']



