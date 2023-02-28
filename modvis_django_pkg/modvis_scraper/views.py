from django.shortcuts import render

# Create your views here.
def modvis_scraper(request):
    return render(request, 'modvis_scraper/modvis_scraper.html', {})

