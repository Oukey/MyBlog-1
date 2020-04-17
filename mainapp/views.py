from django.shortcuts import render
from blogapp.forms import SelectAreaForm
from blogapp.models import Area, GroupKnowledge


def index(request, pk=None):
    title_name = 'Мой блог'
    description = "Мой блог: создай свой блог, делись мыслями и фотографиями."

    if request.method == 'POST':
        form = SelectAreaForm(request.POST)
        keydata = request.POST.get("group_kn")

        context = {'set_title': 'Страница поиска детали',
                   'description': description,
                   'form': form,
                   'keydata': keydata,
                   # 'modyfy_auto': ModyfyAuto.objects.get(pk=keydata),

                   }
        return render(request, 'page2.html', context)
    else:
        form = SelectAreaForm()

        context = {'set_title': title_name,
                   'description': description,
                   'form': form,
                   }
        return render(request, 'index.html', context)


def reload_group(request):
    area_id = request.GET.get('id_area')
    current_group = GroupKnowledge.objects.filter(area_kn=area_id).order_by('name')
    return render(request, 'inc_templates_misc/group_dropdown_list_options.html', {'group_kn': current_group})


def reload_sub_group(request):
    model_id = request.GET.get('model')
    modyfys = ModyfyAuto.objects.filter(model_id=model_id).order_by('name')
    return render(request, 'inc_templates_misc/modyfy_dropdown_list_options.html', {'modyfys': modyfys})
