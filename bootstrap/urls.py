from django.urls import path
from bootstrap import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('services/', views.services, name='services')
]