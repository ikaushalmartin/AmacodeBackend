"""topranker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from top.models import User
from django.urls import path
from .views import index,logout,RegisterView,UserView 
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter


router= DefaultRouter()
 
 
urlpatterns = [
    path('',index,name="index"),
    path('api/auth',RegisterView.as_view(),name="reg"),
    path('api/gettoken',obtain_auth_token,name="login"),
    path('api/user',UserView.as_view(),name="view/delete"),
   
    
    





    # path('getpost/', ProblemPostAPIView.as_view(), name="postproblems"),
    # path('getupdate/<int:id>/', ProblemView.as_view(), name="getproblems"),
    # path('getsubmission/', SubmissionListView.as_view(), name = "Submissionview")

#/(?P<id>\d+)/$
] + router.urls
