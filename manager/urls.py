from django.urls import path


from manager.views import main, LoginCreateView,show_secret_buttons, LoginListView, LoginDetailView, LoginUpdateView

app_name = 'manager'

urlpatterns = [
    path('add-login/', LoginCreateView.as_view(), name='add_login'),
    path('edit-login/<int:pk>/', LoginUpdateView.as_view(), name='edit_login'),
    path('list-logins/', LoginListView.as_view(), name='list_logins'),
    path('detail-login/<int:pk>/', LoginDetailView.as_view(), name='detail_login'),
    path('secret-buttons/', show_secret_buttons, name='secret_buttons'),
    path('', main, name='main'),
]
