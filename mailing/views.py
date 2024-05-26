from random import sample

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from blog.models import BlogView
from mailing.forms import (ClientServiceForm, MailingAttemptForm, MailingForm,
                           MailingFormManager, MessageMailingForm)
from mailing.models import (ClientService, Mailing, MailingAttempt,
                            MessageMailing)


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy("mailing:mailing_list")
    login_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user_ = form.save(commit=False)
        user_.user = self.request.user
        return super().form_valid(form)


class MailingListView(ListView):
    model = Mailing
    form_class = MailingForm
    context_object_name = "mailing"


class MailingDetailView(DetailView):
    model = Mailing
    form_class = MailingForm
    login_url = reverse_lazy("users:login")


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy("mailing:mailing_list")
    login_url = reverse_lazy("users:login")


class MailingManagerUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingFormManager
    success_url = reverse_lazy("mailing:mailing_list")
    login_url = reverse_lazy("users:login")


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy("mailing:mailing_list")
    login_url = reverse_lazy("users:login")


class MailingAttemptListView(ListView):
    model = MailingAttempt
    form_class = MailingAttemptForm
    context_object_name = "mailing"
    login_url = reverse_lazy("users:login")


class MailingAttemptDetailView(DetailView):
    model = MailingAttempt
    form_class = MailingAttemptForm
    context_object_name = "mailing"
    login_url = reverse_lazy("users:login")


class MessageMailingCreateView(LoginRequiredMixin, CreateView):
    model = MessageMailing
    form_class = MessageMailingForm
    success_url = reverse_lazy("mailing:mailing_message_list_view")
    login_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user_ = form.save(commit=False)
        user_.user = self.request.user
        return super().form_valid(form)


class MessageMailingListView(LoginRequiredMixin, ListView):
    model = MessageMailing
    form_class = MessageMailingForm
    context_object_name = "message"
    login_url = reverse_lazy("users:login")


class MessageMailingDetailView(DetailView):
    model = MessageMailing
    form_class = MessageMailingForm
    context_object_name = "message"
    login_url = reverse_lazy("users:login")


class MessageMailingUpdateView(LoginRequiredMixin, UpdateView):
    model = MessageMailing
    form_class = MessageMailingForm
    login_url = reverse_lazy("users:login")


class MessageMailingDeleteView(LoginRequiredMixin, DeleteView):
    model = MessageMailing
    success_url = reverse_lazy("mailing:mailing_message_list_view")
    login_url = reverse_lazy("users:login")


class ClientServiceCreateView(LoginRequiredMixin, CreateView):
    model = ClientService
    form_class = ClientServiceForm
    success_url = reverse_lazy("mailing:client_list_view")
    login_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user_ = form.save(commit=False)
        user_.user = self.request.user
        return super().form_valid(form)


class ClientServiceListView(ListView):
    model = ClientService
    form_class = ClientServiceForm
    context_object_name = "client"
    login_url = reverse_lazy("users:login")


class ClientServiceDetailView(DetailView):
    model = ClientService
    form_class = ClientServiceForm
    context_object_name = "client"
    login_url = reverse_lazy("users:login")


class ClientServiceUpdateView(LoginRequiredMixin, UpdateView):
    model = ClientService
    form_class = ClientServiceForm
    login_url = reverse_lazy("users:login")


class ClientServiceDeleteView(LoginRequiredMixin, DeleteView):
    model = ClientService
    success_url = reverse_lazy("mailing:client_list_view")
    login_url = reverse_lazy("users:login")


class MainPageListView(ListView):
    model = BlogView
    template_name = "mailing/index.html"
    context_object_name = "main_"

    def get_queryset(self):
        queryset = super().get_queryset()
        random_blogs = sample(list(queryset), 3)
        return random_blogs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Подсчет общего количества объектов модели Mailing
        mailing_count = Mailing.objects.count()
        context["mailing_count"] = mailing_count

        # Подсчет количества объектов модели Mailing с условием status_mailing='Запущена'
        started_mailing_count = Mailing.objects.filter(
            status_mailing="Запущена"
        ).count()
        context["started_mailing_count"] = started_mailing_count

        # Подсчет количества объектов модели ClientService
        clientservice_count = ClientService.objects.count()
        context["clientservice_count"] = clientservice_count

        return context
