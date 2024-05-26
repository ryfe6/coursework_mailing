from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from mailing.apps import MailingConfig
from mailing.views import (ClientServiceCreateView, ClientServiceDeleteView,
                           ClientServiceDetailView, ClientServiceListView,
                           ClientServiceUpdateView, MailingAttemptDetailView,
                           MailingAttemptListView, MailingCreateView,
                           MailingDeleteView, MailingDetailView,
                           MailingListView, MailingManagerUpdateView,
                           MailingUpdateView, MainPageListView,
                           MessageMailingCreateView, MessageMailingDeleteView,
                           MessageMailingDetailView, MessageMailingListView,
                           MessageMailingUpdateView)

app_name = MailingConfig.name

urlpatterns = [
    path("", cache_page(60)(MainPageListView.as_view()), name="home_list"),
    path("mailing/list", MailingListView.as_view(), name="mailing_list"),
    path("mailing/create/", MailingCreateView.as_view(), name="mailing_create"),
    path("mailing/<int:pk>", MailingDetailView.as_view(), name="mailing_detail"),
    path("mailing/delete/<int:pk>", MailingDeleteView.as_view(), name="mailing_delete"),
    path("mailing/edit/<int:pk>", MailingUpdateView.as_view(), name="mailing_update"),
    path(
        "mailing/manager/edit/<int:pk>",
        MailingManagerUpdateView.as_view(),
        name="mailing_manager_update",
    ),
    path(
        "mailing/attempt/view",
        MailingAttemptListView.as_view(),
        name="mailing_attempt_list_view",
    ),
    path(
        "mailing/attempt/<int:pk>",
        MailingAttemptDetailView.as_view(),
        name="mailing_attempt_detail",
    ),
    path(
        "mailing/message/view",
        MessageMailingListView.as_view(),
        name="mailing_message_list_view",
    ),
    path(
        "mailing/message/create/",
        MessageMailingCreateView.as_view(),
        name="mailing_message_create",
    ),
    path(
        "mailing/message/<int:pk>",
        MessageMailingDetailView.as_view(),
        name="mailing_message_detail",
    ),
    path(
        "mailing/message/delete/<int:pk>",
        MessageMailingDeleteView.as_view(),
        name="mailing_message_delete",
    ),
    path(
        "mailing/message/edit/<int:pk>",
        MessageMailingUpdateView.as_view(),
        name="mailing_message_update",
    ),
    path(
        "client/view",
        ClientServiceListView.as_view(),
        name="client_list_view",
    ),
    path("client/create/", ClientServiceCreateView.as_view(), name="client_create"),
    path("client/<int:pk>", ClientServiceDetailView.as_view(), name="client_detail"),
    path(
        "client/delete/<int:pk>",
        ClientServiceDeleteView.as_view(),
        name="client_delete",
    ),
    path(
        "client/edit/<int:pk>", ClientServiceUpdateView.as_view(), name="client_update"
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
