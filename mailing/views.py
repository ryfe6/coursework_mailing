from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from mailing.models import Mailing, MailingAttempt, MessageMailing, ClientService

from mailing.forms import MailingAttemptForm, MessageMailingForm, ClientServiceForm, MailingForm


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')

    def form_valid(self, form):
        client = form.save()
        client.user = self.request.user
        client.save()

        return super().form_valid(form)


class MailingListView(ListView):
    model = Mailing
    form_class = MailingForm


class MailingDetailView(DetailView):
    model = Mailing
    form_class = MailingForm


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')


class MailingDeleteView(DeleteView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')


class MailingAttemptCreateView(CreateView):
    model = MailingAttempt
    form_class = MailingAttemptForm


class MailingAttemptListView(ListView):
    model = MailingAttempt
    form_class = MailingAttemptForm
    context_object_name = 'mailing'


class MailingAttemptDetailView(DetailView):
    model = MailingAttempt
    form_class = MailingAttemptForm
    context_object_name = 'mailing'


class MailingAttemptUpdateView(UpdateView):
    model = MailingAttempt
    form_class = MailingAttemptForm
    success_url = reverse_lazy('mailing:mailing_list')


class MailingAttemptDeleteView(DeleteView):
    model = MailingAttempt
    form_class = MailingAttemptForm


class MessageMailingCreateView(CreateView):
    model = MessageMailing
    form_class = MessageMailingForm
    success_url = reverse_lazy('mailing:mailing_message_list_view')

    def form_valid(self, form):
        client = form.save()
        client.user = self.request.user
        client.save()

        return super().form_valid(form)


class MessageMailingListView(ListView):
    model = MessageMailing
    form_class = MessageMailingForm
    context_object_name = 'message'


class MessageMailingDetailView(DetailView):
    model = MessageMailing
    form_class = MessageMailingForm
    context_object_name = 'message'


class MessageMailingUpdateView(UpdateView):
    model = MessageMailing
    form_class = MessageMailingForm


class MessageMailingDeleteView(DeleteView):
    model = MessageMailing
    form_class = MessageMailingForm
    success_url = reverse_lazy('mailing:mailing_message_list_view')


class ClientServiceCreateView(CreateView):
    model = ClientService
    form_class = ClientServiceForm
    reverse_lazy = reverse_lazy('mailing:client_list_view')

    def form_valid(self, form):
        client = form.save()
        client.user = self.request.user
        client.save()

        return super().form_valid(form)


class ClientServiceListView(ListView):
    model = ClientService
    form_class = ClientServiceForm


class ClientServiceDetailView(DetailView):
    model = ClientService
    form_class = ClientServiceForm


class ClientServiceUpdateView(UpdateView):
    model = ClientService
    form_class = ClientServiceForm


class ClientServiceDeleteView(DeleteView):
    model = ClientService
    form_class = ClientServiceForm
    reverse_lazy = reverse_lazy('mailing:client_list_view')
