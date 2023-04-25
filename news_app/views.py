from django.shortcuts import render
from rest_framework.response import Response
from news_app.models import Post
from news_app.serializer import PostSerializer
from rest_framework import status
from rest_framework.views import APIView 
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth.models import User
from news_app.serializer import UserSerializer
from rest_framework import permissions
from news_app.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
class UserDetail(generics.RetrieveAPIView): 
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
   
   
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

     
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
     queryset = Post.objects.all()
     serializer_class = PostSerializer
     permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
     
    
    
    
    
    
   