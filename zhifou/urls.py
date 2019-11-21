"""zhifou URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

from web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.login),
    path('register/',views.regiter),
    path('article/articleCurd/', views.articleCurd),      #显示全部数据
    path('article/delArticleByID/',views.delArticleByID), #删除数据
    path('article/updateArticle/',views.updateArticle),  #更新数据页面
    path('article/saveArticle',views.saveArticle),       # 保存数据
    path('article/addArticlePage/',views.addArticlePage),
    path('article/addArticle/',views.addArticle),

    path('article/showArticle/', views.showArticle),  # 显示全部数据
    path('article/articleDetails/',views.articleDetails),

    path('photo/', views.photo),
    path('uploadphoto/',views.uploadphoto),

    path('query/',views.query)
]
