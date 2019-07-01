from django.urls import path

from apps.core import views

urlpatterns = [
    path('',
         views.Index.as_view(),
         name="index"),
    path('preview/<slug:str>/',
         views.ArticleDetail.as_view(),
         name="article-preview"),
]
