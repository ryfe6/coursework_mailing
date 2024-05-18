from django.urls import path

from mailing.views import (MailingCreateView, MailingListView, MailingUpdateView, MailingDetailView, MailingDeleteView,
                           MailingAttemptListView, MailingAttemptCreateView, MailingAttemptDeleteView,
                           MailingAttemptUpdateView, MailingAttemptDetailView, MessageMailingListView, MessageMailingCreateView,
                           MessageMailingDeleteView, MessageMailingDetailView, MessageMailingUpdateView,
                           ClientServiceListView, ClientServiceCreateView, ClientServiceDetailView,
                           ClientServiceDeleteView, ClientServiceUpdateView)
from django.conf.urls.static import static
from django.conf import settings
from mailing.apps import MailingConfig
app_name = MailingConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='mailing_list'),
    path('mailing/create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing/<int:pk>', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing/delete/<int:pk>', MailingDeleteView.as_view(), name='mailing_delete'),
    path('mailing/edit/<int:pk>', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing/attempt/view', MailingAttemptListView.as_view(), name='mailing_attempt_list_view'),
    path('mailing/attempt/create/', MailingAttemptCreateView.as_view(), name='mailing_attempt_create'),
    path('mailing/attempt/<int:pk>', MailingAttemptDetailView.as_view(), name='mailing_attempt_detail'),
    path('mailing/attempt/delete/<int:pk>', MailingAttemptDeleteView.as_view(), name='mailing_attempt_delete'),
    path('mailing/attempt/edit/<int:pk>', MailingAttemptUpdateView.as_view(), name='mailing_attempt_update'),
    path('mailing/message/view', MessageMailingListView.as_view(), name='mailing_message_list_view'),
    path('mailing/message/create/', MessageMailingCreateView.as_view(), name='mailing_message_create'),
    path('mailing/message/<int:pk>', MessageMailingDetailView.as_view(), name='mailing_message_detail'),
    path('mailing/message/delete/<int:pk>', MessageMailingDeleteView.as_view(), name='mailing_message_delete'),
    path('mailing/message/edit/<int:pk>', MessageMailingUpdateView.as_view(), name='mailing_message_update'),
    path('client/view', ClientServiceListView.as_view(), name='client_list_view'),
    path('client/create/', ClientServiceCreateView.as_view(), name='client_create'),
    path('client/<int:pk>', ClientServiceDetailView.as_view(), name='client_detail'),
    path('client/delete/<int:pk>', ClientServiceDeleteView.as_view(), name='client_delete'),
    path('client/edit/<int:pk>', ClientServiceUpdateView.as_view(), name='client_update'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
