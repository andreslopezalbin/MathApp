from django.shortcuts import render

from MathApp.services import get_equation


def main(request):
    request.session['current'] = 0

    if request.session.get('best') is None:
        request.session['best'] = 0

    return render(request, 'main.html')


def init(request):
    context = get_equation()
    request.session['current'] = 0
    return render(request, 'game.html', context)


def play(request):
    context = get_equation()
    request.session['current'] = request.session.get('current') + 1

    if request.session.get('current') > request.session.get('best'):
        request.session['best'] = request.session.get('current')

    return render(request, 'game.html', context)
