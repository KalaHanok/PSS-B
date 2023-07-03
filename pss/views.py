from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile,AttendanceModel,BtechModel
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.parsers import JSONParser
from django.core.serializers import serialize
from .serializers import Profile_Serializer,AttendanceSerializer,BtechSerializer
from rest_framework.parsers import JSONParser
from django.core.serializers.json import DjangoJSONEncoder
import io
from rest_framework_simplejwt.authentication import JWTAuthentication
import json
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
class ProfileInfo(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def put(self,request,format=None):
        serialized_data=Profile_Serializer(Profile.objects.get(pk=request.user.id),data=request.data,partial=True)
        if serialized_data.is_valid():
            serialized_data.save()
        # print(data)
        return Response({"msg":"suucess"})
    def  get(self,request):
        serialized_data=Profile_Serializer(Profile.objects.get(pk=request.user))
        return Response(serialized_data.data)  
class AddProfile(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAdminUser]
    def post(self,request,format=None):
        serialize_data=Profile_Serializer(data=request.data)
        if serialize_data.is_valid():
            serialize_data.save()
class AddAttendance(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAdminUser]
    def post(self,request,format=None):
        data=request.data.dict()
        userid=data['studentid']
        print(data)
        data['studentid']=User.objects.get(username=userid).id
        print(data)
        serialize_data=AttendanceSerializer(data=data)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response({"msg":'recorded your response successfully'})
        return Response({'msg':'attendanced is not marked'})
class GetAttendance(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        serialize=AttendanceSerializer(AttendanceModel.objects.filter(studentid=request.user.id),many=True)
        return Response(serialize.data)
class AddBtechInfo(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAdminUser]
    def post(self,request,format=None):
        data=request.data.dict()
        userid=data['user']
        data['user']=User.objects.get(username=userid).id
        serialize_data=BtechSerializer(data=data)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response({"msg":'recorded your response successfully'})
        return Response({'msg':'attendanced is not marked'})
class GetBtechInfo(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        serialize=BtechSerializer(BtechModel.objects.filter(user=request.user.id).order_by('yr','sem'),many=True)
        return Response(serialize.data)