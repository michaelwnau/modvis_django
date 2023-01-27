from django.shortcuts import render

# Create your views here.
def hello_world(request):
    return render(request, 'helloapp/hello_world.html', {})