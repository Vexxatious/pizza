# Generated by Django 4.1 on 2022-08-25 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_galerifoto_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='galerifoto',
            name='isim',
            field=models.CharField(default='obje', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menu',
            name='isim',
            field=models.CharField(default='obje', max_length=50),
            preserve_default=False,
        ),
    ]
