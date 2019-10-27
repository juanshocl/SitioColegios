import uuid
from django.db import models
from django.db.models import Avg

# Create your models here.

class SchoolType(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Description = models.CharField(max_length=20)

    def __str__(self):
        return str(self.Id)

class User(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Email = models.CharField(max_length=45)
    Phone = models.CharField(max_length=12)
    Name = models.CharField(max_length=15)
    Last_Name = models.CharField(max_length=15)
    
    def __str__(self):
        return str(self.Id)

class state_province(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Name = models.CharField(max_length=25)
    
    def __str__(self):
        return str(self.Id)      

class School(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Name = models.CharField(max_length=40)
    RatingShool = models.FloatField() #models.FloatField(null=True, blank=True, default=None)
    ImageMD = models.ImageField(upload_to='photos/modal')
    ImageProfile = models.ImageField(upload_to='photos/profile')
    Address = models.CharField(max_length=60)
    State_Province = models.OneToOneField(state_province, on_delete=models.CASCADE)
    Phone = models.CharField(max_length=12)
    Type = models.ForeignKey(SchoolType, on_delete=models.CASCADE)
    Review = models.TextField(max_length=200)

    def __str__(self):
        return str(self.Id)
    
    def average_rating(self):
        return self.review_set.aggregate(Avg('Rating'))['rating__avg'] #Promedio de las evaluaciones.

class Ratings(models.Model):
    RATING = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    Rating = models.IntegerField(choices=RATING)
    Schools = models.ManyToManyField(School)

    def __str__(self):
        return str(self.Id)