from django.contrib import admin

from mailling_list.models import Mailling_list, Client, MailingLogs, Message


@admin.register(Mailling_list)
class MaillingListAdmin(admin.ModelAdmin):
    list_display = ('mailing_time', 'frequency', 'status',)
    list_filter = ('mailing_time', 'status', 'client',)
    search_fields = ('client', 'status', 'mailing_time',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name',)
    list_filter = ('full_name',)
    search_fields = ('email',)


@admin.register(MailingLogs)
class MailingLogsAdmin(admin.ModelAdmin):
    list_display = ('attempt_time', 'status', 'responce',)
    list_filter = ('attempt_time', 'status',)
    search_fields = ('status',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'body',)