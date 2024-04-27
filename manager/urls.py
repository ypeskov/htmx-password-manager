from django.urls import path


from manager.views import main

app_name = 'manager'

urlpatterns = [
    path('', main, name='main'),
]
