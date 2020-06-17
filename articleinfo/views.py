from django.shortcuts import render
from .models import ArticleInfo

def article(request):
    articles_info = ArticleInfo.objects
    return render(request, 'articleinfo/articles.html',{'articles_info':articles_info})