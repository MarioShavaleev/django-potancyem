from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import Horoscope #импортируем данные из БД
from django.shortcuts import get_object_or_404


def index(request):
    zodiacs = Horoscope.objects.all()
    # for zodiac in zodiacs: # делается для записи/перезаписи slug потом убирается
    #     zodiac.save()
    context = {'zodiacs': zodiacs}
    return render(request, 'horoscope/index.html', context=context)

def get_info_about_sign_zodiac(request, slug_zodiac:str):
    zodiac = get_object_or_404(Horoscope, slug=slug_zodiac)
    zodiacs = Horoscope.objects.all()
    data = {'zodiac': zodiac, 'zodiacs': zodiacs}
    return render(request, 'horoscope/info_zodiac.html', context=data)#context передал данные в info_zodiac.html

# до slug
# def get_info_about_sign_zodiac(request, sign_zodiac:int):
#     zodiac = Horoscope.objects.get(id=sign_zodiac)
#     zodiacs = Horoscope.objects.all()
#     data = {'zodiac': zodiac, 'zodiacs': zodiacs}
#     return render(request, 'horoscope/info_zodiac.html', context=data)#context передал данные в info_zodiac.html
