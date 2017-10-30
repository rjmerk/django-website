from django.conf.urls import url

from apps.core.views import IndexView

urlpatterns = [
    url(r'^$',
        IndexView.as_view(),
        name="index"),
]
