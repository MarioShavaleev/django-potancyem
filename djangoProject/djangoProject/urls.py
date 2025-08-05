
from django.contrib import admin
from django.urls import path, include
from horoscope import views
from debug_toolbar.toolbar import debug_toolbar_urls

from horoscope.views import Otziv_UpdateView, OtzivView, ListFeedBack, DetailFeedBack, DoneView

admin.site.site_header = 'Админка сайта'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('otziv/', OtzivView.as_view(), name='otziv'),
    path('done/', DoneView.as_view(), name='done'),
    path('list/', ListFeedBack.as_view(), name='list_feedback'),
    path('<int:id_otziv>/', Otziv_UpdateView.as_view(), name='update_otziv'),
    path('', include('horoscope.urls')),
    path('detail/<int:pk>/', DetailFeedBack.as_view(), name='detailFeedBack'),
] + debug_toolbar_urls()
