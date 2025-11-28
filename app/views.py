from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import StudentForm
from .models import Student

def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        # print(form)
        if form.is_valid():
            # print(form.cleaned_data)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            contact = form.cleaned_data['contact']
            image = form.cleaned_data.get('image')
            file = form.cleaned_data.get('file')

            Student.objects.create(name=name,email=email,contact=contact,image=image,file=file)
            return HttpResponse(f"Data save successfully!<br>Name: {name}<br>Email: {email}")
        else:
            return render(request, 'home.html', {'fm': form})

    else:
        form = StudentForm()
        return render(request, 'home.html', {'fm': form})
