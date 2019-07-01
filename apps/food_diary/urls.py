from django.urls import path

from apps.food_diary import views

urlpatterns = [
    path('',
         views.Index.as_view(),
         name="index"),
]
