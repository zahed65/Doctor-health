from django.urls import path
from . import views



urlpatterns = [
    path('index/', views.index, name='index'),
    path('articles/', views.article_list, name='articles'),
    path('articles/<slug:slug>/', views.article_detail, name='article_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
