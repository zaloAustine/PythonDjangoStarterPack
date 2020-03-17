# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from v1.serializer import QuizSerializer,QuestionSerializer,ProfileSerializer
from v1.models import Quiz,Question,Profile
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import AllowAny
from v1.serializer import UserSerializer


# Create your views here.

class QuizesView(APIView):    
    permission_classes = (IsAuthenticated,) 
    def get_object(self):
        try:
            return Quiz.objects.all()
        except:
            raise Quiz.objects.all()

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)    

    def get(self,request,format=None):
        queryset = self.get_object()
        serializer = QuizSerializer(queryset,many = True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    
    def post(self,request):
        serializer = QuizSerializer(data = request.data)
        try:
            if serializer.is_valid():
                serializer.save(owner = self.request.user.id) 
                return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

    

    def delete(self,request):
        querySet = Quiz.objects.get(id = request.data['id']) 
        querySet.delete()
        return Response(data='DELETE',status=status.HTTP_410_GONE)       


    def put(self,request):
        quiz = Quiz.objects.get(id = request.data['id'])    
        serializer = QuizSerializer(quiz,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_202_ACCEPTED)

        return Response(data=serializer.data,status=status.HTTP_404_NOT_FOUND)



@api_view(['POST'])
def create_user(request):
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def user_specificData(request):
        owner = Quiz.objects.get(owner = request.data['owner'])    
        serializer = QuizSerializer( Quiz.objects.filter(owner = owner).all(),many = True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
   



