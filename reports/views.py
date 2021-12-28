from django.shortcuts import render


def home_view(request):
    hello = 'Hello from the view'
    return render(request, 'reports/main.html', {'hello': hello})
