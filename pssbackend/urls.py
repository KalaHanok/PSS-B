"""
URL configuration for pssbackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from pss import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/addUsers/',views.addStudents.as_view(),name="addStudents"),
    path('api/profileinfo/',views.ProfileInfo.as_view(),name='profile'),
    path('api/addattendance/',views.AddAttendance.as_view(),name="attendence"),
    path('api/getAttendance/',views.GetAttendance.as_view(),name='getAttandence'),
    path('api/addprofile',views.AddProfile.as_view(),name="addProfile"),
    path('api/addbtechinfo/',views.AddBtechInfo.as_view(),name='addbtechinfo'),
    path('api/getbtechinfo/',views.GetBtechInfo.as_view(),name='getbtechinfo'),
    path('api/adddiplomainfo/',views.AddDiplomaInfo.as_view(),name='adddiplomainfo'),
    path('api/getdiplomainfo/',views.GetDiplomaInfo.as_view(),name='getdiplomainfo'),
    path('api/addfeedetails/',views.AddFeeDetails.as_view(),name="addfeedetails"),
    path('api/getfeedetails/',views.GetFeeDetails.as_view(),name='getfeedetails'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)