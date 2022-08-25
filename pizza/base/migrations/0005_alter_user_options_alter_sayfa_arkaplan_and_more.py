# Generated by Django 4.1 on 2022-08-25 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_sayfa_fotograf'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': 'Kullanıcılar'},
        ),
        migrations.AlterField(
            model_name='sayfa',
            name='arkaplan',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='sayfa',
            name='baslik',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sayfa',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='sayfa',
            name='yazi',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
