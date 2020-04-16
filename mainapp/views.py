from django.shortcuts import render


def index(request):
    title_name = 'Личный сайт для тестов'
    description = "Личный сайт для тестов: новости и примеры работ."

    context = {'set_title': title_name, 'description': description}
    return render(request, 'index.html', context)
