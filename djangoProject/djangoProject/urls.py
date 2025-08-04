
from django.contrib import admin
from django.urls import path, include
from horoscope import views
from debug_toolbar.toolbar import debug_toolbar_urls

from horoscope.views import done, Otziv_UpdateView, OtzivView

admin.site.site_header = 'Админка сайта'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('otziv/', OtzivView.as_view(), name='otziv'),
    path('done/', done, name='done'),
    path('<int:id_otziv>/', Otziv_UpdateView.as_view(), name='update_otziv'),
    path('', include('horoscope.urls')),
] + debug_toolbar_urls()
