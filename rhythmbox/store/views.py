from django.shortcuts import render

def index(request):
    """
    Landing/Welcome page for website.
    """
    return render(request, 'store/index.html')
