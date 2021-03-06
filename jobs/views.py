from django.shortcuts import render
from .serializer import HallSerializer,ConditionSerializer 
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Hall,Condition,Img
import requests

class HallList(APIView):
    def get(self,request):
        hall=Hall.objects.all()
        serializer=HallSerializer(hall,many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = HallSerializer(data=request.data)
        if serializer.is_valid():
            print("step1")
            question = serializer.save()
            print("step2")
            serializer = HallSerializer(question)
            print("herererere")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

        # url="https://swapi.dev/api/people/1/"
        # response=requests.get(url)
        # data=response.json()
        # print(data['vehicles'])
        return Response(None)
    


    # def put(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     print("snippet-->",snippet)
    #     serializer = CruxSerializer(snippet, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def get(self,request,pk):
    #     print("helloss",pk)
    #     crux=Crux.objects.filter(firstName=str(pk))
    #     print("crux",crux)
    #     serializer=CruxSerializer(crux,many=True)
    #     print("hello",serializer.data)
    #     return Response(serializer.data,status=status.HTTP_201_CREATED)

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


