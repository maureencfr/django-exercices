
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import SuperHero
from .forms import SuperHeroForm
from django.shortcuts import redirect

def index(request):
    heroes = SuperHero.objects.all()
    return render(request, 'heroes/index.html', {'heroes': heroes})

def detail(request, id):
    hero = get_object_or_404(SuperHero, id=id)
    return render(request, 'heroes/detail.html', {'hero': hero})


def ajouter_hero(request):
    if request.method == 'POST':
        form = SuperHeroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SuperHeroForm()

    return render(request, 'heroes/ajouter.html', {'form': form})
