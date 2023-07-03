from rest_framework import serializers
from .models import Profile,SchoolModel,AttendanceModel,BtechModel
class Profile_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=('user','first_name','middle_name','last_name','profile_pic','phone_num','address')
class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model=SchoolModel
        fields=('user','study','telugu','hindi','english','social','math','physics','biology','pass_yr','ispass')
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=AttendanceModel
        fields=('studentid','date','ispresent')
class BtechSerializer(serializers.ModelSerializer):
    class Meta:
        model=BtechModel
        fields=('user','yr','sem','subject','marks')

