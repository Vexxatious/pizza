# Generated by Django 4.1 on 2022-08-26 16:30

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_galerifoto_fotograf_alter_sayfa_arkaplan_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sayfa',
            name='fotograf',
            field=models.ImageField(blank=True, null=True, upload_to='', validators=[base.models.foto_validator]),
        ),
    ]
