from django import forms
from .models import InformSalary

class SalaryForm(forms.ModelForm):
    class Meta:
        model = InformSalary
        fields = ['date_check', 'summ_check', 'date_next_raise']
        labels = {'date_check': 'Дата назначения зп','summ_check' :'Сумма зарплаты', 'date_next_raise': 'Дата следующего повышения'}



