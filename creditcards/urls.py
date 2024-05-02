from django.urls import path


from .views import (CreditCardCreateView, CreditCardListView, CreditCardDetailView,
                    CreditCardUpdateView, CreditCardDeleteView)

app_name = 'creditcards'

urlpatterns = [
    path('add/', CreditCardCreateView.as_view(), name='add_creditcard'),
    path('list/', CreditCardListView.as_view(), name='list_creditcards'),
    path('detail/<int:pk>/', CreditCardDetailView.as_view(), name='detail_creditcard'),
    path('update/<int:pk>/', CreditCardUpdateView.as_view(), name='update_creditcard'),
    path('delete/<int:pk>/', CreditCardDeleteView.as_view(), name='delete_creditcard'),
]
