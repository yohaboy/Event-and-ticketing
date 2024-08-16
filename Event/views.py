from typing import Any
from django.shortcuts import render
from django.views.generic import (CreateView
                                  ,UpdateView,
                                  DeleteView,
                                  ListView)
from Event.models import EventModel

#views

class Home(ListView):
    model = EventModel
    template_name = 'Event/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = EventModel.objects.all()
        return context

