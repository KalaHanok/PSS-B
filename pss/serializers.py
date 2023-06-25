from rest_framework import serializers
from .models import Profile
class Profile_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=('user','first_name','middle_name','last_name','profile_pic')
