from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'home.html') # This view renders the home.html template when the home_view function is called.
# The request parameter is the HTTP request object that Django passes to the view function.