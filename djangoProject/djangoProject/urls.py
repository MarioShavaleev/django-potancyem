
from django.contrib import admin
from django.urls import path, include
from horoscope import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('horoscope/', include('horoscope.urls')),

]
