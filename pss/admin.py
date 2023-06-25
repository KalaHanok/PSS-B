from django.contrib import admin
from .models import Profile
# Register your models here.
@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display=('user','first_name','middle_name','last_name','profile_pic')