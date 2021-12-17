from django.contrib import admin
from django.urls import path, include
from .views import FeedView, CommentView

urlpatterns = [
    path('feed/', FeedView.as_view()),
    path('comment/', CommentView.as_view()),

]
