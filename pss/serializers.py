from rest_framework import serializers
from .models import Profile,SchoolModel,AttendanceModel,BtechModel,DiplomaModel,FeeModel,GroceriesModel
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
class DiplomaSerializer(serializers.ModelSerializer):
    class Meta:
        model=DiplomaModel
        fields=('user','yr','sem','subject','marks')

class FeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=FeeModel
        fields=('user','date','particulars','amount','recipt')

class GroceriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroceriesModel
        fields=('name','stock','unit','stock_added_date')