from catalog.models import School, Ratings, ContactModel, state_province, SchoolType
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class ShoolSerializer(ModelSerializer):
    class Meta:
        model = School
        fields = ['Id', 'Name', 'Score', 'groups', 'ImageMD', 'ImageProfile', 'Address', 'State_Province',\
            'Phone', 'Type', 'Review']


