from django.shortcuts import render, redirect
from .models import Fruit
from .forms import FruitForm

def fruit_list(request):
    fruits = Fruit.objects.all()
    return render(request, 'fruit_list.html', {'fruits': fruits})

def fruit_detail(request, pk):
    fruit = Fruit.objects.get(pk=pk)
    return render(request, 'fruit_detail.html', {'fruit': fruit})

def fruit_create(request):
    if request.method == 'POST':
        form = FruitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fruit_list')
    else:
        form = FruitForm()
    return render(request, 'fruit_form.html', {'form': form})

def fruit_update(request, pk):
    fruit = Fruit.objects.get(pk=pk)
    if request.method == 'POST':
        form = FruitForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('fruit_list')
    else:
        form = FruitForm(instance=fruit)
    return render(request, 'fruit_form.html', {'form': form})

def fruit_delete(request, pk):
    fruit = Fruit.objects.get(pk=pk)
    fruit.delete()
    return redirect('fruit_list')