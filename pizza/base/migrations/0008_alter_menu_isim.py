# Generated by Django 4.1 on 2022-08-25 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_galerifoto_isim_menu_isim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='isim',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
