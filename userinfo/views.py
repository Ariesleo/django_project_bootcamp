from django.shortcuts import render
from .models import UserInfo
from projectlistinfo.models import ProjectListInfo


def home(request):
    projlist_info = ProjectListInfo.objects
    user_info = UserInfo.objects
    return render(request, 'userinfo/home.html',{'user_info': user_info, 'projlist_info':projlist_info})
