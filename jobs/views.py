from django.shortcuts import render
from .serializer import HallSerializer,ConditionSerializer,ImageSerializer
from rest_framework import serializers,status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Hall,Condition,Img

class HallList(APIView):
    def get(self,request):
        hall=Hall.objects.all()
        serializer=HallSerializer(hall,many=True)
        return Response(serializer.data)

class Images(APIView):
    def get(self,request):
        images=Img.objects.all()
        serializer=ImageSerializer(images,many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            question = serializer.save()
            serializer = ImageSerializer(question)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


