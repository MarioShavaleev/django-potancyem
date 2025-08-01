
from django.contrib import admin
from django.urls import path, include
from horoscope import views
from debug_toolbar.toolbar import debug_toolbar_urls

admin.site.site_header = 'Админка сайта'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('horoscope.urls')),
] + debug_toolbar_urls()
