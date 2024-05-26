from django import forms
from django.core.exceptions import ValidationError
from django.forms import BooleanField

from users.models import User

from .models import ClientService, Mailing, MailingAttempt, MessageMailing


class StyleFormMixin:
    """Миксин класс для красивого вывода форм."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class MailingForm(StyleFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MailingForm, self).__init__(*args, **kwargs)
        us = User.objects.all()
        for u in us:
            self.fields["client"].queryset = ClientService.objects.filter(user=u.id)
            self.fields["message"].queryset = MessageMailing.objects.filter(user=u.id)

    class Meta:
        model = Mailing
        fields = ["quit_at", "next_send_time", "period_mailing", "client", "message"]


class MailingFormManager(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Mailing
        fields = [
            "status_mailing",
        ]


class MailingAttemptForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = MailingAttempt
        fields = "__all__"


# Форма для модели MessageMailing
class MessageMailingForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = MessageMailing
        fields = ["subject_line", "body"]


# Форма для модели ClientService
class ClientServiceForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = ClientService
        fields = ["email", "name", "comments"]
