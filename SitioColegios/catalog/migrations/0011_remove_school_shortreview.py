# Generated by Django 2.2.6 on 2019-11-06 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20191106_2041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='ShortReview',
        ),
    ]