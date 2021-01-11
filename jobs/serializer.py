from rest_framework import serializers
from .models import Hall,Condition,Img


class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Condition
        fields=['day','time','status','mems']




class HallSerializer(serializers.ModelSerializer):
    condition=ConditionSerializer(many=True,read_only=False)
    class Meta:
        model=Hall
        fields=['name','maxcapacity','vacancy','condition']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Img
        fields=['title','image']
