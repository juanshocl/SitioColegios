# Generated by Django 2.2.6 on 2019-11-16 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0022_contactomodel_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactomodel',
            name='Rut',
            field=models.CharField(default=None, max_length=14),
        ),
    ]
