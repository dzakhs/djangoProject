from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Count
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from blog.models import Blog
from mailling_list.forms import MaillingForm, MessageForm
from mailling_list.models import Mailling_list, Message, MailingLogs, Client


class IndexListView(ListView):
    model = Mailling_list
    template_name = 'mailling_list/index.html'

    def get(self, request, *args, **kwargs):
        mailling_list_count = Mailling_list.objects.count()
        mailling_list_count_active = Mailling_list.objects.filter(status='started').count()
        blogs = list(Blog.objects.order_by('?').values_list('title', flat=True)[:3])
        unique_clients_count = Client.objects.annotate(mailling_num=Count('mailling_list')).filter(mailling_num__gt=0).count()

        context = {
            'title': "Главная",
            'mailling_list_count': mailling_list_count,
            'mailling_list_count_active': mailling_list_count_active,
            'unique_clients_count': unique_clients_count,
            'blogs': blogs
        }

        return render(request, 'mailling_list/index.html', context)


class MaillingListView(ListView):
    model = Mailling_list
    template_name = 'mailling_list/mailling.html'




class MaillingCreateView(CreateView):
    model = Mailling_list
    form_class = MaillingForm
    success_url = reverse_lazy('mailling_list:mailling')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        MessageFormset = inlineformset_factory(Mailling_list, Message, exclude=('mailling_list', ), extra=1)
        if self.request.method == 'POST':
            formset = MessageFormset(self.request.POST)
        else:
            formset = MessageFormset()

        context_data['formset'] = formset

        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = self.get_context_data()['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class MaillingUpdateView(UpdateView):
    model = Mailling_list
    form_class = MaillingForm
    success_url = reverse_lazy('mailling_list:mailling')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        MessageFormset = inlineformset_factory(Mailling_list, Message, exclude=('mailling_list', ), extra=1)
        if self.request.method == 'POST':
            formset = MessageFormset(self.request.POST)
        else:
            formset = MessageFormset(instance=self.object)

        context_data['formset'] = formset

        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = self.get_context_data()['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

class MaillingDeleteView(UserPassesTestMixin, DeleteView):
    model = Mailling_list
    success_url = reverse_lazy('mailling_list:mailling')

    #def test_func(self):
    #    return self.request.user.is_superuser


class MaillingDetailView(DetailView):
    model = Mailling_list



class MaillingLogsListView(ListView):
    model = MailingLogs
    template_name = 'mailling_list/mailling_logs.html'
