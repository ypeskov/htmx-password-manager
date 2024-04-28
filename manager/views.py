import logging

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_GET
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from manager.forms import LoginForm
from manager.models import Login

logger = logging.getLogger(__name__)


@login_required
@require_GET
def main(request):
    return render(request, 'manager/main.html')


@login_required
@require_GET
def show_secret_buttons(request):
    return render(request, 'manager/secret-buttons.html')


@method_decorator(login_required, name='dispatch')
class LoginCreateView(CreateView):
    model = Login
    form_class = LoginForm
    template_name = 'manager/login_form.html'
    success_url = reverse_lazy('manager:secret_buttons')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class LoginUpdateView(UpdateView):
    model = Login
    form_class = LoginForm
    template_name = 'manager/login_form.html'

    def form_valid(self, form):
        super().form_valid(form)
        return render(self.request, 'manager/login_detail.html', {'object': self.object})

    def get_success_url(self):
        return reverse('manager:detail_login', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
class LoginListView(ListView):
    template_name = 'manager/login_list.html'

    def get_queryset(self):
        return Login.objects.filter(user=self.request.user)


@method_decorator(login_required, name='dispatch')
class LoginDetailView(DetailView):
    template_name = 'manager/login_detail.html'

    def get_queryset(self):
        return Login.objects.filter(user=self.request.user)
