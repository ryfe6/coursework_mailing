from django import forms
from django.forms import BooleanField
from .models import MessageMailing, ClientService, Mailing, MailingAttempt


class StyleFormMixin:
    """Миксин класс для красивого вывода форм."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class MailingForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = '__all__'


class MailingAttemptForm(forms.ModelForm):
    class Meta:
        model = MailingAttempt
        fields = '__all__'


# Форма для модели MessageMailing
class MessageMailingForm(forms.ModelForm):
    class Meta:
        model = MessageMailing
        fields = ['subject_line', 'body', 'user']
        widgets = {
            'subject_line': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
        }


# Форма для модели ClientService
class ClientServiceForm(forms.ModelForm):
    class Meta:
        model = ClientService
        fields = ['email', 'name', 'comments', 'user']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'comments': forms.Textarea(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
        }

