from django.conf.urls import url, include
from .views import ProductView, BrandView
from django.urls import path


urlpatterns = [
    path('product/', ProductView.as_view(), name='file-upload'),
    path('brand/', BrandView.as_view()),
]