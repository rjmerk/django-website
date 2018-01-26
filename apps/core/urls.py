from django.conf.urls import url

from apps.core import views

urlpatterns = [
    url(r'^$',
        views.Index.as_view(),
        name="index"),
    url(r'^preview/(?P<slug>[-\w]+)/$',
        views.ArticleDetail.as_view(),
        name="article-preview"),
]
