from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from icecream import ic

from .models import CreditCard
from .forms import CreditCardForm

ic.configureOutput(includeContext=True)


@method_decorator(login_required, name='dispatch')
class CreditCardCreateView(CreateView):
    model = CreditCard
    form_class = CreditCardForm
    template_name = 'manager/item_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('creditcards:detail_creditcard', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Add Credit Card'
        context['create_url_name'] = "creditcards:add_creditcard"
        return context


@method_decorator(login_required, name='dispatch')
class CreditCardListView(ListView):
    template_name = 'creditcards/creditcard_list.html'

    def get_queryset(self):
        return CreditCard.objects.filter(user=self.request.user)


@method_decorator(login_required, name='dispatch')
class CreditCardDetailView(DetailView):
    template_name = 'creditcards/cc_detail.html'

    def dispatch(self, request, *args, **kwargs):
        ic(request)
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return CreditCard.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['card'] = context['object']
        return context


@method_decorator(login_required, name='dispatch')
class CreditCardUpdateView(UpdateView):
    model = CreditCard
    form_class = CreditCardForm
    template_name = 'manager/item_form.html'

    def form_valid(self, form):
        super().form_valid(form)
        return render(self.request, 'creditcards/cc_detail.html', {'card': self.object})

    def get_success_url(self):
        return reverse('creditcards:detail_creditcard', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Edit Credit Card Details'
        context['update_url_name'] = "creditcards:update_creditcard"
        context['back_url'] = reverse('creditcards:detail_creditcard', kwargs={'pk': self.object.pk})
        return context


@method_decorator(login_required, name='dispatch')
class CreditCardDeleteView(DeleteView):
    model = CreditCard
    success_url = reverse_lazy('creditcards:list_creditcards')
