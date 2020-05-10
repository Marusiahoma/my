from django.shortcuts import render


def index(request):
    return render(request, 'mainApp/homePage.html')


def contact(request):
    return render(request, 'mainApp/basic.html', {'values':["Если у вас есть предложения, писать на почту:", "m2003tut.by", "polygold@yandex.ru", "sofiashatova251@gmail.com"]})
