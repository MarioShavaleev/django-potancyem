from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import Horoscope, Otziv #импортируем данные из БД
from django.shortcuts import get_object_or_404
from .forms import OtzivForm
from django.views import View

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


# def otziv(request):
#     if request.method == 'POST':
#         form = OtzivForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return HttpResponseRedirect('/done')
#     else:
#         form = OtzivForm()
#     return render(request, 'horoscope/otziv.html', context={'form': form})
class OtzivView(View):
    def get(self, request):
        form = OtzivForm(request.POST)
        return render(request, 'horoscope/otziv.html', context={'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = OtzivForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/done')
            return render(request, 'horoscope/otziv.html', context={'form': form})

# def update_otziv(request, id_otziv:int):
#     feed = get_object_or_404(Otziv, id=id_otziv)
#     if request.method == 'POST':
#         form = OtzivForm(request.POST, instance=feed)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(f'/{id_otziv}')
#     else:
#         form = OtzivForm(instance=feed)
#     return render(request, 'horoscope/otziv.html', context={'form': form})
class Otziv_UpdateView(View):
    def get(self, request, id_otziv:int):
        feed = get_object_or_404(Otziv, id=id_otziv)
        form = OtzivForm(instance=feed)
        return render(request, 'horoscope/otziv.html', context={'form': form})

    def post(self, request, id_otziv:int):
        feed = get_object_or_404(Otziv, id=id_otziv)
        if request.method == 'POST':
            form = OtzivForm(request.POST, instance=feed)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/done')
            return render(request, 'horoscope/otziv.html', context={'form': form})

def done(request):
    return render(request, 'horoscope/done.html')