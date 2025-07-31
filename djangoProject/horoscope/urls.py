from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('horoscope/<str:slug_zodiac>/', views.get_info_about_sign_zodiac, name='get_info_about_sign_zodiac'),

    # было до slug
    #path('horoscope/<int:sign_zodiac>/', views.get_info_about_sign_zodiac, name='get_info_about_sign_zodiac'),

]
