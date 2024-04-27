from django.urls import path


from manager.views import main, LoginCreateView,show_secret_buttons

app_name = 'manager'

urlpatterns = [
    path('add-login/', LoginCreateView.as_view(), name='add_login'),
    path('secret-buttons/', show_secret_buttons, name='secret_buttons'),
    path('', main, name='main'),
]
