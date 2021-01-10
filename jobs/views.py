from django.shortcuts import render
from .serializer import HallSerializer,ConditionSerializer
from rest_framework import serializers,status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Hall,Condition

class HallList(APIView):
    def get(self,request):
        hall=Hall.objects.all()
        serializer=HallSerializer(hall,many=True)
        return Response(serializer.data)
