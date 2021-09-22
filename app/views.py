from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from app.forms import CarrosForm
from app.models import Carros
from django.core.paginator import Paginator

# Create your views here.

'''
  Funções para renderização do meu template
'''
def home(request):
  # data = {'db': Carros.objects.all()}
  data = {}

  search = request.GET.get('search')
  if search:
    data['db'] = Carros.objects.filter(modelo__icontains = search)
  else:
    data['db'] = Carros.objects.all()

  # all = Carros.objects.all()
  # paginator = Paginator(all, 5)
  # pages = request.GET.get('page')
  # data['db'] = paginator.get_page(pages)

  return render(request, 'index.html', data)

def form(request):
  data = {'form': CarrosForm()}
  return render(request, 'form.html', data)

def create(request):
  form = CarrosForm(request.POST or None)
  if form.is_valid():
    form.save()
    return HttpResponseRedirect("/")
  # return render(request, 'form.html')

def view(request, pk):
  data = {'db': Carros.objects.get(pk=pk)}
  return render(request, 'view.html', data)

def edit(request, pk):
  data = {}
  data['db'] = Carros.objects.get(pk=pk)
  data['form'] = CarrosForm(instance=data['db'])
  return render(request, 'form.html', data)

def update(request, pk):
  data = {}
  data['db'] = Carros.objects.get(pk=pk)
  form = CarrosForm(request.POST or None, instance=data['db'])
  if form.is_valid():
    form.save()
    return HttpResponseRedirect("/")

def delete(request, pk):
  db = Carros.objects.get(pk=pk)
  db.delete()
  return HttpResponseRedirect("/")