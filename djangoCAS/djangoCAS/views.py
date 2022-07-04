from django.http import HttpResponse


def index(request):
    if request.user.is_authenticated:
        return HttpResponse('<p>Вы вошли как <strong>%s</strong>.</p><p><a href="/cas/logout">Выйти</a></p>' % request.user)
    else:
        return HttpResponse('<a href="/cas/login">Войти</a>')
