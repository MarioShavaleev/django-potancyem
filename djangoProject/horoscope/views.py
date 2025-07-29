from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


def index(request):
    #rez +=   f"<li><a href='{redirect_path}'>{sign.title()}</a></li>"
    zodiacs = list(zodiac_dict)
    context = {'zodiacs':zodiacs}
    return render(request, 'horoscope/index.html', context=context)

def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    data = {'description': description, 'sign': sign_zodiac}
    return render(request, 'horoscope/info_zodiac.html', context=data)#context передал данные в info_zodiac.html

def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f'Неправильный порядковый номер')
    name_zodiac = zodiacs[sign_zodiac-1]
    redirect_url = reverse('horoscope-name', args=[name_zodiac])
    return HttpResponseRedirect(redirect_url)

zodiac_dict = {
    'aries': 'Овен - первый знак зодиака. Рожден 21 марта - 20 апреля',
    'taurus': 'Телец - второй знак зодиака. Рожден 21 апреля - 21 мая',
    'gemini': 'Близнецы - третий знак зодиака. Рожден 22 мая - 21 июня',
    'cancer': 'Рак - четвёртый знак зодиака. Рожден 22 июня - 22 июля',
    'leo': 'Лев - пятый знак зодиака. Рожден 23 июля - 21 августа',
    'virgo': 'Дева - шестой знак зодиака. Рожден 22 августа - 23 сентября',
    'libra': 'Весы - седьмой знак зодиака. Рожден 24 сентября - 23 октября',
    'scorpio': 'Скорпион - восьмой знак зодиака. Рожден 24 октября - 22 ноября',
    'sagittarius': 'Стрелец - девятый знак зодиака. Рожден 23 ноября - 21 декабря',
    'capricorn': 'Козерог - десятый знак зодиака. Рожден 22 декабря - 20 января',
    'aquarius': 'Водолей - одиннадцатый знак зодиака. Рожден 21 января - 19 февраля',
    'pisces': 'Рыбы - двенадцатый знак зодиака. Рожден 20 февраля - 20 марта'
}
