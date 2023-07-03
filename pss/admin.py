from django.contrib import admin
from .models import Profile,SchoolModel,AttendanceModel,BtechModel
# Register your models here.
@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display=('user','first_name','middle_name','last_name','profile_pic','address','phone_num')
@admin.register(SchoolModel)
class AdminSchool(admin.ModelAdmin):
    list_display=('user','study','telugu','hindi','english','social','math','physics','biology','pass_yr','ispass')
@admin.register(AttendanceModel)
class AdminAttendance(admin.ModelAdmin):
    list_display=('studentid','date','ispresent')
@admin.register(BtechModel)
class AdminBtech(admin.ModelAdmin):
    list_display=('user','yr','sem','subject','marks')
