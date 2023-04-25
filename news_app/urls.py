from django.urls import path
from news_app import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('news_app', views.PostList.as_view()),
    path ('news_app/<int:pk>/', views.PostDetail.as_view()),
    path('users/',views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)