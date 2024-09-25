from django.shortcuts import render

def index(request):
    """
    Placeholder view for the main page of my_app.
    This view renders a simple template and can be expanded later.
    """
    return render(request, 'my_app/index.html')
