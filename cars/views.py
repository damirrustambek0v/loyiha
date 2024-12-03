from django.shortcuts import render, redirect

from.models import Cars

def cars_list(request):
    cars = Cars.objects.all()
    ctx = {'cars': cars}
    return render(request, 'cars/cars-list.html',ctx)


def cars_create(request):
    name = request.POST.get('name')
    model  = request.POST.get('model')
    year = request.POST.get('year')
    if name and model and year:
        Cars.objects.create(
            name=name,
            model=model,
            year=year,
        )
        return redirect('cars:cars_list')
    return render(request, 'cars/cars-form.html')

