from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    response = f"""
        Hello, world! <br><br>
        Это проект на джанге, здесь будут разные приложение для вашего удобства
        """
    return HttpResponse(response)


def about(request):
    response = f"""
            About me
            <ul>
                <li>Мое имя: Кирилл</li>
                <li>Мой возраст: 21 год</li>
                <li>Это мой второй проект на джанге</li>
            </ul>
            """
    return HttpResponse(response)

