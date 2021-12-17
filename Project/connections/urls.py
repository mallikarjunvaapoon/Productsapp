from django.contrib import admin
from django.urls import path, include
from .views import SenderView, RequestView, ReceivedView, UpdateView

urlpatterns = [
    path('sender/', SenderView.as_view()),
    path('received/', ReceivedView.as_view()),
    path('request/', RequestView.as_view()),
    path('update/', UpdateView.as_view()),

]
