from rest_framework import serializers
from .models import Hall,Condition,Img,Film


class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Condition
        fields=['day','time','status','mems']

class FilmSerialzer(serializers.ModelSerializer):
    class Meta:
        model=Film
        fields=['film']


class HallSerializer(serializers.ModelSerializer):
    condition=ConditionSerializer(many=True,read_only=False)
    films=FilmSerialzer(many=True,read_only=False)
    class Meta:
        model=Hall
        fields=['name','maxcapacity','vacancy','condition','films']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Img
        fields=['title','image']
