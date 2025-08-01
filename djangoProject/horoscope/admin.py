from django.contrib import admin
from .models import Horoscope
# Register your models here.

#'''изменяем отображение таблицы в админке'''
# class HoroscopeAdmin(admin.ModelAdmin): #можно так
#     list_display = ['title', 'peoples', 'cost']
# admin.site.register(Horoscope, HoroscopeAdmin)

#'''через декоратор'''
@admin.register(Horoscope)
class HoroscopeAdmin(admin.ModelAdmin):
    list_display = ['title', 'peoples', 'cost'] # какие поля отображаем в админке
    # здесь регистрировать отдельно модель не надо (без - admin.site.register(Horoscope))
    list_editable = ['cost', 'peoples']
    list_per_page = 6
    search_fields = ['title__istartswith']
    fields = ['title', 'peoples', 'cost']


