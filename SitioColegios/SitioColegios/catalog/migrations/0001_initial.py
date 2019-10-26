# Generated by Django 2.2.6 on 2019-10-26 04:28

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='state_province',
            fields=[
                ('Id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Last_Name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('Id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=40)),
                ('Ratings', models.IntegerField()),
                ('Image', models.ImageField(upload_to='photos')),
                ('Address', models.CharField(max_length=60)),
                ('Phone', models.CharField(max_length=12)),
                ('Review', models.TextField(max_length=200)),
                ('State_Province', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='catalog.state_province')),
                ('Type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.SchoolType')),
            ],
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('Id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('Schools', models.ManyToManyField(to='catalog.School')),
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='catalog.User')),
            ],
        ),
    ]
