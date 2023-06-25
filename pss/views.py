from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.
class addStudents(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    def post(self,request,format=None):
        data=request.data
        userName = data['username']
        userPass = data['password']
        userCpass = data['confirmpass']
        if  len(User.objects.filter(username=userName)) == 0 and userPass==userCpass :
            user = User.objects.create_user(userName, None, userPass)
            user.save()
            return Response({
                'message':'user has saved successfully'
            })
        return Response({
            'message':'user is not saved'
        })
class Login(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        user=request.user
        data=Profile.objects.get(pk=user)

        return Response({'msg':'hello'})