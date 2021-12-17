from django.contrib import admin
from django.urls import path, include
from .views import Register, Login, UserView, Update, NotificationsView, Send_request
from rest_framework import routers



router = routers.DefaultRouter()
router.register('send', Send_request),

urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', Login.as_view()),
    path('user/', UserView.as_view()),
    path('update/', Update.as_view()),
    path('notification/', NotificationsView.as_view()),
    path('', include(router.urls)),

]
