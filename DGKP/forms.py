from django import forms
from django.forms import ModelForm
from dateutil.relativedelta import relativedelta
import datetime
from .models import *


class Breaking_Form(ModelForm):
    class Meta:
        model = Breaking
        fields = ['breaking_full_name',
                  'breaking_room',
                  'breaking_category',
                  'breaking_description',
                  'breaking_email'
                  ]
        labels = {
            'breaking_full_name': 'ФИО',
            'breaking_room': 'Кабинет',
            'breaking_category': 'Категория',
            'breaking_description': 'Описание',
            'breaking_email': 'Электронная почта'
        }
        widgets = {
            'breaking_date': forms.DateInput(attrs={'type': 'date', 'style': 'color: white;', 'class': 'date-input'}),
        }


class Breaking_Form_Admin(forms.ModelForm):
    class Meta:
        model = Breaking
        fields = [
            'breaking_full_name',
            'breaking_email',
            'breaking_date',
            'breaking_room',
            'breaking_category',
            'breaking_description',
            'breaking_status',
            'breaking_worker_fullname',

        ]
        labels = {
            'breaking_full_name': 'ФИО',
            'breaking_date': 'Дата',
            'breaking_room': 'Кабинет',
            'breaking_category': 'Категория',
            'breaking_description': 'Описание',
            'breaking_status': 'Статус',
            'breaking_worker_fullname': 'Отвественный',
            'breaking_email': 'Электронная почта'
        }


class Material_Form(ModelForm):
    class Meta:
        model = Material
        fields = ['material_name']
        labels = {
            'material_name': 'Название'
        }


class BreakingMaterial_Form(forms.ModelForm):
    class Meta:
        model = BreakingMaterial
        fields = ['breaking', 'material', 'quantity']
        labels = {
            'breaking': 'Заявка',
            'material': 'Материал',
            'quantity': 'Количество'
        }

    def __init__(self, breaking_id, *args, **kwargs):
        super(BreakingMaterial_Form, self).__init__(*args, **kwargs)
        self.fields['breaking'].initial = breaking_id if breaking_id else None


class Staff_Form(forms.ModelForm):
    class Meta:
        model = Staff
        fields = [
            'staff_fullname',
            'staff_phone_number',
            'staff_category'
        ]
        labels = {
            'staff_fullname': 'ФИО работника',
            'staff_phone_number': 'Тел. номер',
            'staff_category': 'Категория'
        }
