from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView

from .models import Node, Title
from .forms import NodeForm, TitleForm


class TitleListView(ListView):
    model = Title


class TitleCreateView(CreateView):
    model = Title
    form_class = TitleForm

    def form_valid(self, form):
        f = form.save(commit=False)
        f.user = self.request.user
        f.save()
        return super(TitleCreateView, self).form_valid(form)

class NodeListView(ListView):
    model = Node

    def get_context_data(self, **kwargs):
        context = super(NodeListView, self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['titletitle'] = Title.objects.get(pk=pk)
        context['sortedinherit'] = Node.objects.filter(title=pk).order_by('inherit')
        return context


class NodeCreateView(CreateView):
    model = Node
    form_class = NodeForm

    def form_valid(self, form):
        f = form.save(commit=False)
        f.status = 'improved'
        pk = self.kwargs['pk']
        f.inherit = pk
        f.user = self.request.user
        titletest = Node.objects.get(pk=pk)
        f.title = titletest.title
        f.save()
        return super(NodeCreateView, self).form_valid(form)
