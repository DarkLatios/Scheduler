from rest_framework import serializers
from .models import Hall,Condition


class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Condition
        fields=['day','time','status']




class HallSerializer(serializers.ModelSerializer):
    condition=ConditionSerializer(many=True,read_only=False)
    class Meta:
        model=Hall
        fields=['name','maxcapacity','vacancy','condition']
