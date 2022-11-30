from django.shortcuts import render
from Articles.models import Entry

# Create your views here.
def home (request):
    articulos= Entry.objects.all()
    return render(request, "welcome.html", {"articulos":articulos})