from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET


@login_required
@require_GET
def main(request):
    return render(request, 'manager/main.html')
