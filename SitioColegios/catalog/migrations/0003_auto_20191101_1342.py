# Generated by Django 2.2.6 on 2019-11-01 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20191027_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='ImageMD',
            field=models.ImageField(upload_to='static/img//modal'),
        ),
        migrations.AlterField(
            model_name='school',
            name='ImageProfile',
            field=models.ImageField(upload_to='static/img/profile'),
        ),
    ]