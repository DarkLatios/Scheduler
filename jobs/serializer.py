from rest_framework import serializers
from .models import Hall,Condition,Film,Img


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Img
        fields=['title','image']

class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Condition
        fields=['day','time','status','mems']
    
    def create(self,validated_data):
        print("hertererte")
        films=validated_data.pop('films')
        condition=validated_data.pop('condition')
        print("Validated data after pop-->",validated_data)
        print("films-->",films)
        print("condition-->",condition)
        user=Hall.objects.create(**validated_data)
        print("user-->",user)
        # for each in choice_data:
            
        #     each['crux']=user
        #     print("each-->",each)
        #     Choice.objects.create(**each)
        return user

class FilmSerialzer(serializers.ModelSerializer):
    class Meta:
        model=Film
        fields=['film']
    
    def create(self,validated_data):
        print("hertererte")
        films=validated_data.pop('films')
        condition=validated_data.pop('condition')
        print("Validated data after pop-->",validated_data)
        print("films-->",films)
        print("condition-->",condition)
        user=Hall.objects.create(**validated_data)
        print("user-->",user)
        # for each in choice_data:
            
        #     each['crux']=user
        #     print("each-->",each)
        #     Choice.objects.create(**each)
        return user


class HallSerializer(serializers.ModelSerializer):
    condition=ConditionSerializer(many=True,read_only=False)
    films=FilmSerialzer(many=True,read_only=False)
    class Meta:
        model=Hall
        fields=['name','maxcapacity','vacancy','floors','condition','films']
    
    def create(self,validated_data):
        print("hertererte")
        films=validated_data.pop('films')
        condition=validated_data.pop('condition')
        print("Validated data after pop-->",validated_data)
        print("films-->",films)
        print("condition-->",condition)
        user=Hall.objects.create(**validated_data)
        print("user-->",user)
        for each in films:
            each['hall']=user
            print("each-->",each)
            Film.objects.create(**each)
        for each in condition:
            each['hall']=user
            Condition.objects.create(**each)
        return user
    
    def update(self, instance, validated_data):
        print("validated data in update-->",validated_data)
        val=validated_data.pop('films')
        print("validated data in update-->",instance)
        # instance=instance[0]
        # instance.firstName=validated_data.get("firstName",instance.firstName)#either change the value if given or remain same as original instance.
        # instance.lastName=validated_data.get("lastName",instance.lastName)
        #instance.save()
        #print("choice set-->",val)
        return instance


