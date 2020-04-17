from django import forms
from .models import Area, GroupKnowledge


class SelectAreaForm(forms.Form):
    area = forms.ModelChoiceField(queryset=Area.objects.all(), label='Область знаний')
    group_kn = forms.ModelChoiceField(queryset=GroupKnowledge.objects.all(), label='Тема')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['group_kn'].queryset = GroupKnowledge.objects.none()
