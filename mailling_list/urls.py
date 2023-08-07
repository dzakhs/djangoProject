from django.conf.urls.static import static
from django.urls import path

from django.conf import settings
from mailling_list.apps import MailingListConfig
from mailling_list.views import IndexListView, MaillingListView, MaillingCreateView, MaillingUpdateView, \
    MaillingDeleteView, MaillingDetailView, MaillingLogsListView, ClientListView, ClientCreateView, ClientUpdateView, \
    ClientDeleteView, ClientDetailView

app_name = MailingListConfig.name

urlpatterns = [
    path('', IndexListView.as_view(), name='homepage'),
    path('mailling/', MaillingListView.as_view(),name='mailling'),
    path('mailling_create/', MaillingCreateView.as_view(), name='mailling_create'),
    path('mailling_update/<int:pk>/', MaillingUpdateView.as_view(), name='mailling_update'),
    path('mailling_delete/<int:pk>/', MaillingDeleteView.as_view(), name='mailling_delete'),
    path('mailling_detail/<int:pk>/', MaillingDetailView.as_view(), name='mailling_detail'),
    path('mailling_logs/', MaillingLogsListView.as_view(), name='mailling_logs'),
    path('client_list/', ClientListView.as_view(), name='clients'),
    path('client_create/', ClientCreateView.as_view(), name='client_create'),
    path('client_update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client_delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
    path('client_detail/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)