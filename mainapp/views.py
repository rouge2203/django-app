from django.shortcuts import render,redirect
from .models import Person

def index(request):
    if request.method == 'POST':
        person = Person.objects.create(
            name = request.POST['name'],
            age = request.POST['age']
        )
        person.save()
        return redirect(index)
        
    return render(request,'index.html')

