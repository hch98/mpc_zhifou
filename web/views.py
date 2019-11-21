import random
from datetime import datetime, time

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.serializers import json
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


#render：讲请求的页面结果提交给客户端
#HttpResponseRedirect  重定向，不需要向客户端呈现数据，而是转回到其它页面
from django.db import models

from web.models import Article, Type, User


def login(request):
    #指定要访问的页面
    return render(request,'login.html')
#注册页面
def regiter(request):
    return render(request,'regiter.html')


#查询所有文章
def articleCurd(request):
    list = Article.objects.all()
    type=Type.objects.all()
    return render(request,'showArticle.html',{'articleList':list,'typeList':type})


#查询发表的文章
def showArticle(request):
    list = Article.objects.filter(flag=1)
    type=Type.objects.all()
    return render(request,'showArticle.html',{'articleList':list,'typeList':type})


#查询发表文章，并分页显示
def query(request):
    type = Type.objects.all()
    limit = 2 # 每页显示的记录数
    articleList = Article.objects.filter(flag=1)
    paginator = Paginator(articleList, limit)  # 实例化一个分页对象
    page = request.GET.get('page')  # 获取页码
    try:
        articleList = paginator.page(page)  # 获取某页对应的记录
    except PageNotAnInteger:  # 如果页码不是个整数
        articleList = paginator.page(1)  # 取第一页的记录
    except EmptyPage:  # 如果页码太大，没有相应的记录
        articleList = paginator.page(paginator.num_pages)  # 取最后一页的记录
    return render_to_response('showArticle.html',{'articleList':articleList,'typeList':type})



#文章详情
def articleDetails(request):
    id=request.GET['id'];
    article=Article.objects.get(article_id=id)

    article.page_view += 1
    article.save(update_fields=['page_view'])   #update_fields 只更新浏览量，加快速率

    return render_to_response('articleDetails.html',{'article':article})



#删除数据
def delArticleByID(request):
    id=request.GET['id'];
    article=Article.objects.get(article_id=id)
    article.delete()
    return HttpResponseRedirect("/article/articleCurd")

#更新一条文章数据
def updateArticle(request):
    id=request.GET['id'];
    article=Article.objects.get(article_id=id)
    return render_to_response('update.html',{'article':article})


#修改文章数据
def saveArticle(request):
   # c={} POST方式获取
   article_id=request.POST['article_id']
   title=request.POST['title']
   content=request.POST['content']
   type_id=request.POST['type_id']
   flag=request.POST['flag']
   account = User.objects.get(user_account='S02')   #外键
   article = Article(article_id=article_id, title=title, content=content, type_id=type_id, user_account=account
                       , flag=flag, create_time=datetime.now())
   if  len(article_id)  > 0 :
       print("id不是null")
   article.save()
   return HttpResponseRedirect("/article/articleCurd")


def addArticlePage(request):
    type = Type.objects.all()
    return render(request, 'add.html',{'typeList':type})



#添加文章数据
@csrf_exempt
def addArticle(request):
   # c={} POST方式获取
   title=request.POST['title']
   content=request.POST['content']
   type_id=request.POST['type_id']
   flag=request.POST['flag']
   usercount=request.POST['user_account']
   account = User.objects.get(user_account=usercount)   #外键 获取发布者
   article = Article(title=title, content=content, type_id=type_id, user_account=account
                       , flag=flag, create_time=datetime.now())
   article.save()
   return HttpResponseRedirect("/article/articleCurd")


def photo(request):
    #指定要访问的页面
    return render(request,'photo.html')


#图片上传
def uploadphoto(request):
        file_obj = request.FILES.get('photo')
        file_name = 'static/uploadimg'+'_'+datetime.now().strftime("%Y%m%d%H%M%S")+'.'+file_obj.name.split('.')[-1] ##以.为分割f符，保留最后一段
        if file_obj.name.split('.')[-1] not in ['jpeg','jpg','png','JPEG','JPG','PNG']:
            return HttpResponse('输入文件有误')
        try:
            with open(file_name,'wb+') as f:
                f.write(file_obj.read())
        except Exception as e:
            print(e)
        return HttpResponse('OK')

