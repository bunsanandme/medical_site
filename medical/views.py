from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import LoginForm, PacientForm, PreprocedureCardForm
from django.contrib.auth.decorators import login_required
from .models import Pacient, PreprocedureCard
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q, F


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def home(request):
    amount_pacient = Pacient.objects.all()
    return render(request, "admin_panel.html", {"amount_pacient": len(amount_pacient)})


@login_required
def show_pacient(request, pacient_id):
        pacient = get_object_or_404(Pacient, pacient_id=pacient_id)
        form = PacientForm(instance=pacient)
        cards = PreprocedureCard.objects.filter(pacient_id=pacient)
        return render(request, 'pacient.html', {'pacient': pacient, 'form': form, "cards": cards})


@login_required
def add_pacient(request):
    if request.method == 'POST':
        form = PacientForm(data=request.POST)
        if form.is_valid():
            new_pacient = form.save(commit=False)
            pacient = Pacient.objects.create(name=new_pacient.name, surname=new_pacient.surname, date_birth=new_pacient.date_birth, gender=new_pacient.gender)
            pacient.save()
            new_form = PacientForm(data=pacient)
            return redirect(f'/pacient/{pacient.pacient_id}', {'pacient': pacient})
    else:
        form = PacientForm()
    return render(request,
                  'add_pacient.html',
                 {"form": form})

@login_required
def action_with_pacient(request, pacient_id):
    if "deletepacient" in request.POST:
        pacient = Pacient.objects.get(pacient_id=pacient_id)
        cards = PreprocedureCard.objects.filter(pacient_id=pacient_id)
        cards.delete()
        pacient.delete()
        return redirect("/pacient/all")
    else:
        form = PacientForm(data=request.POST)
        if form.is_valid():
            pacient = Pacient.objects.get(pacient_id=pacient_id)
            new_pacient = form.save(commit=False)
            pacient.name=new_pacient.name
            pacient.surname=new_pacient.surname
            pacient.date_birth=new_pacient.date_birth
            pacient.gender=new_pacient.gender
            pacient.save()
            cards = PreprocedureCard.objects.filter(pacient_id=pacient_id)
        return redirect(f'/pacient/{pacient.pacient_id}', {'pacient': pacient, "cards": cards})

@login_required
def edit_pacient(request, pacient_id):
    pacient = Pacient.objects.get(pacient_id=pacient_id)
    form = PacientForm()
    return redirect(f'/pacient/{pacient.pacient_id}', {'pacient': pacient})

@login_required
def show_all_pacients(request):
    object_list = Pacient.objects.all() 
    paginator = Paginator(object_list, 4)
    page = request.GET.get('page')
    try:
        pacients = paginator.page(page)
    except PageNotAnInteger:
        pacients = paginator.page(1)
    except EmptyPage:
        pacients = paginator.page(paginator.num_pages)
    return render(request, "pacient_list.html",
                  {'page': page,
                   'pacients': pacients})

@login_required
def search_pacient(request):
    results = []
    if request.method == "GET":
        query = request.GET.get('search', None)
        if query == '':
             pacients = Pacient.objects.all()
        else:
            Pacient.objects.annotate(fullname=(F("name")+F("surname")))
            pacients = Pacient.objects.filter(Q(name__icontains=query) | Q(surname__icontains=query))
        paginator = Paginator(pacients, 4)
        page = request.GET.get('page')
        try:
            pacients = paginator.page(page)
        except PageNotAnInteger:
            pacients = paginator.page(1)
        except EmptyPage:
            pacients = paginator.page(paginator.num_pages)
        return render(request, "pacient_list.html",
                  {'page': page,
                   'pacients': pacients})

@login_required
def show_card(request, card_id):
    card = PreprocedureCard.objects.get(card_id=card_id)
    form = PreprocedureCardForm(instance=card)
    return render(request, "pacient_card.html", {"card": card, "form": form})

@login_required
def add_new_card(request, pacient_id):
    card = PreprocedureCard(pacient_id=Pacient.objects.get(pacient_id=pacient_id))
    card.save()
    form = PreprocedureCardForm(instance=card)
    return render(request, "pacient_card.html", {"card": card, "form": form})

def test(request):
    return render(request, "pacient_card.html")