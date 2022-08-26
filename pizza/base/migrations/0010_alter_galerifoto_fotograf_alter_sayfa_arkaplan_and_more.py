# Generated by Django 4.1 on 2022-08-26 16:29

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_mailadresi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galerifoto',
            name='fotograf',
            field=models.ImageField(upload_to='', validators=[base.models.galeri_validator]),
        ),
        migrations.AlterField(
            model_name='sayfa',
            name='arkaplan',
            field=models.ImageField(blank=True, null=True, upload_to='', validators=[base.models.background_validator]),
        ),
        migrations.AlterField(
            model_name='sayfa',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='', validators=[base.models.logo_validator]),
        ),
    ]