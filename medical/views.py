from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import LoginForm, MedicalHistoryForm, PacientForm, PreprocedureCardForm, SurgicalHistoryForm, GastrointestinalProcedureForm, UrologicalProcedureForm, SurgicalProceduralDetailForm, RoboticArmLocationForm, TrocardLocationForm, BloodLossForm, RobotMalfunctionForm, InstrumentsUsedForm
from django.contrib.auth.decorators import login_required
from .models import Pacient, PreprocedureCard, Card, MedicalHistory, SurgicalHistory, GastrointestinalProcedure, UrologicalProcedure, SurgicalProceduralDetail, RoboticArmLocation, TrocardLocation, BloodLoss, RobotMalfunction, InstrumentUsed
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


def home(request):
    amount_pacient = Pacient.objects.all()
    return render(request, "admin_panel.html", {"amount_pacient": len(amount_pacient)})

@login_required
def show_pacient(request, pacient_id):
        pacient = get_object_or_404(Pacient, pacient_id=pacient_id)
        form = PacientForm(instance=pacient)
        cards = Card.objects.filter(pacient_id=pacient)
        return render(request, 'pacient.html', {'pacient': pacient, 'form': form, "cards": cards, })


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
            print(form.errors.as_text())
            return render(request,
                  'add_pacient.html',
                    {"form": form})
    else:
        form = PacientForm()
    return render(request,
                  'add_pacient.html',
                    {"form": form})

@login_required
def action_with_pacient(request, pacient_id):
    if request.method == 'POST':
        pacient = Pacient.objects.get(pacient_id=pacient_id)
        cards = Card.objects.filter(pacient_id=pacient_id)
        if "deletepacient" in request.POST:
            cards.delete()
            pacient.delete()
            return redirect("/pacient/all")
        else:
            form = PacientForm(data=request.POST)
            if form.is_valid():
                new_pacient = form.save(commit=False)
                pacient.name = new_pacient.name
                pacient.surname = new_pacient.surname
                pacient.date_birth = new_pacient.date_birth
                pacient.gender = new_pacient.gender
                pacient.save()
                cards = Card.objects.filter(pacient_id=pacient_id)
            else:
                return render(request, 'pacient.html', {'pacient': pacient, 'form': form, "cards": cards, })
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
            if not query.isdigit():
                pacients = Pacient.objects.filter(Q(name__icontains=query) | Q(surname__icontains=query))
            else:
                pacients = Pacient.objects.filter(Q(pacient_id__contains=int(query)))
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
    card = Card.objects.get(card_id=card_id)
    form_preproc = PreprocedureCardForm(instance=PreprocedureCard.objects.get(card_id=card))
    form_mh = MedicalHistoryForm(instance=MedicalHistory.objects.get(card_id=card))
    form_sh = SurgicalHistoryForm(instance=SurgicalHistory.objects.get(card_id=card))
    form_gp = GastrointestinalProcedureForm(instance=GastrointestinalProcedure.objects.get(card_id=card))
    form_up = UrologicalProcedureForm(instance=UrologicalProcedure.objects.get(card_id=card))
    form_spd = SurgicalProceduralDetailForm(instance=SurgicalProceduralDetail.objects.get(card_id=card))
    form_ral = RoboticArmLocationForm(instance=RoboticArmLocation.objects.get(card_id=card))
    form_tl = TrocardLocationForm(instance=TrocardLocation.objects.get(card_id=card)),
    form_bl = BloodLossForm(instance=BloodLoss.objects.get(card_id=card))
    form_rm = RobotMalfunctionForm(instance=RobotMalfunction.objects.get(card_id=card))
    form_iu = InstrumentsUsedForm(instance=InstrumentUsed.objects.get(card_id=card))
    InstrumentUsed
    context = {"card": card, 
                "form_preproc": form_preproc, 
                "form_mh": form_mh,
                "form_sh": form_sh,
                "form_gp": form_gp,
                "form_up": form_up,
                "form_spd": form_spd,
                "form_ral": form_ral,
                "form_tl": form_tl,
                "form_bl": form_bl,
                "form_rm": form_rm,
                "form_iu": form_iu,}
    return render(request, "pacient_card.html", context)

@login_required
def add_new_card(request, pacient_id):
    card = Card(pacient_id=Pacient.objects.get(pacient_id=pacient_id))
    card.save()
    preprocedure = PreprocedureCard(card_id = card)
    preprocedure.save()
    medical_history = MedicalHistory(card_id = card)
    medical_history.save()
    surgical_history = SurgicalHistory(card_id = card)
    surgical_history.save()
    gastro_procedure = GastrointestinalProcedure(card_id = card)
    gastro_procedure.save()
    uro_procedure = UrologicalProcedure(card_id = card)
    uro_procedure.save()
    surg_proc_detail = SurgicalProceduralDetail(card_id = card)
    surg_proc_detail.save()
    rob_arm_location = RoboticArmLocation(card_id = card)
    rob_arm_location.save()
    trocard_location = TrocardLocation(card_id = card)
    trocard_location.save()
    blood_loss = BloodLoss(card_id = card)
    blood_loss.save()
    robot_malf = RobotMalfunction(card_id = card)
    robot_malf.save()
    inst_used = InstrumentUsed(card_id = card)
    inst_used.save()
    return redirect(show_card, card.get_id())

@login_required
def edit_card(request, card_id):
    if "editcard" in request.POST:
        card = PreprocedureCard.objects.get(card_id=Card.objects.get(card_id=card_id))
        form = PreprocedureCardForm(data=request.POST)
        print(form.errors)
        if form.is_valid():
            new_card = form.save(commit=False)
            card.creation_date = new_card.creation_date
            card.admission_date = new_card.admission_date
            card.sign_date = new_card.sign_date
            card.is_smoker = new_card.is_smoker
            card.packyears = new_card.packyears
            card.height = new_card.height
            card.weight = new_card.weight
            card.save()
            card = Card.objects.get(card_id=card_id)
            form = PreprocedureCardForm(instance=card)
            return redirect(show_card, card.get_id())
        else:
            card = Card.objects.get(card_id=card_id)
            return redirect(show_card, card.get_id())

@login_required
def edit_medical_history(request, card_id):
    if "editcard" in request.POST:
        card = MedicalHistory.objects.get(card_id=Card.objects.get(card_id=card_id))
        form = MedicalHistoryForm(data=request.POST)
        if form.is_valid():
            new_card = form.save(commit=False)
            card = new_card
            card.history_card_id = MedicalHistory.objects.get(card_id=Card.objects.get(card_id=card_id)).history_card_id
            card.card_id = Card.objects.get(card_id=card_id)
            card.save()
        return redirect(show_card, card_id)

@login_required
def edit_surgical_history(request, card_id):
    if "editcard" in request.POST:
        card = SurgicalHistory.objects.get(card_id=Card.objects.get(card_id=card_id))
        form = SurgicalHistoryForm(data=request.POST)
        if form.is_valid():
            new_card = form.save(commit=False)
            card.has_abdominal_surgery = new_card.has_abdominal_surgery
            card.surgion_description = new_card.surgion_description
            card.save()
        return redirect(show_card, card_id)

@login_required
def edit_gastro_procedure(request, card_id):
    if "editcard" in request.POST:
        card = GastrointestinalProcedure.objects.get(card_id=Card.objects.get(card_id=card_id))
        form = GastrointestinalProcedureForm(data=request.POST)
        if form.is_valid():
            new_card = form.save(commit=False)
            card = new_card
            card.gastro_procedure_id = GastrointestinalProcedure.objects.get(card_id=Card.objects.get(card_id=card_id)).gastro_procedure_id
            card.card_id = Card.objects.get(card_id=card_id)
            card.save()
        return redirect(show_card, card_id)

@login_required
def edit_uro_procedure(request, card_id):
    if "editcard" in request.POST:
        card = UrologicalProcedure.objects.get(card_id=Card.objects.get(card_id=card_id))
        form = UrologicalProcedureForm(data=request.POST)
        if form.is_valid():
            new_card = form.save(commit=False)
            card = new_card
            card.uro_procedure_id = UrologicalProcedure.objects.get(card_id=Card.objects.get(card_id=card_id)).uro_procedure_id
            card.card_id = Card.objects.get(card_id=card_id)
            card.save()
        return redirect(show_card, card_id)

@login_required
def edit_spd(request, card_id):
    if "editcard" in request.POST: 
        card = SurgicalProceduralDetail.objects.get(card_id=Card.objects.get(card_id=card_id))
        form = SurgicalProceduralDetailForm(data=request.POST)
        if form.is_valid():
            new_card = form.save(commit=False)
            card = new_card
            card.surg_proc_detail_id = SurgicalProceduralDetail.objects.get(card_id=Card.objects.get(card_id=card_id)).surg_proc_detail_id
            card.card_id = Card.objects.get(card_id=card_id)
            card.save()
        return redirect(show_card, card_id)

@login_required
def edit_ral(request, card_id):
    if "editcard" in request.POST: 
            card = RoboticArmLocation.objects.get(card_id=Card.objects.get(card_id=card_id))
            form = RoboticArmLocationForm(data=request.POST)
            print(form.errors)
            if form.is_valid():
                new_card = form.save(commit=False)
                card = new_card
                card.robotic_arm_loc_id = RoboticArmLocation.objects.get(card_id=Card.objects.get(card_id=card_id)).robotic_arm_loc_id
                card.card_id = Card.objects.get(card_id=card_id)
                card.save()
            return redirect(show_card, card_id)

@login_required
def edit_tl(request, card_id):
    if "editcard" in request.POST: 
            card = TrocardLocation.objects.get(card_id=Card.objects.get(card_id=card_id))
            form = TrocardLocationForm(data=request.POST)
            print(form.errors)
            if form.is_valid():
                new_card = form.save(commit=False)
                card = new_card
                card.trocard_location_id = TrocardLocation.objects.get(card_id=Card.objects.get(card_id=card_id)).trocard_location_id
                card.card_id = Card.objects.get(card_id=card_id)
                card.save()
            return redirect(show_card, card_id)

@login_required
def edit_bl(request, card_id):
    if "editcard" in request.POST: 
            card = BloodLoss.objects.get(card_id=Card.objects.get(card_id=card_id))
            form = BloodLossForm(data=request.POST)
            print(form.errors)
            if form.is_valid():
                new_card = form.save(commit=False)
                card = new_card
                card.blood_loss_id = BloodLoss.objects.get(card_id=Card.objects.get(card_id=card_id)).blood_loss_id
                card.card_id = Card.objects.get(card_id=card_id)
                card.save()
            return redirect(show_card, card_id)

@login_required
def edit_rm(request, card_id):
    if "editcard" in request.POST: 
            card = RobotMalfunction.objects.get(card_id=Card.objects.get(card_id=card_id))
            form = RobotMalfunctionForm(data=request.POST)
            print(form.errors)
            if form.is_valid():
                new_card = form.save(commit=False)
                card = new_card
                card.rob_mal_id = RobotMalfunction.objects.get(card_id=Card.objects.get(card_id=card_id)).rob_mal_id
                card.card_id = Card.objects.get(card_id=card_id)
                card.save()
            return redirect(show_card, card_id)

@login_required
def edit_iu(request, card_id):
    if "editcard" in request.POST: 
            card = InstrumentUsed.objects.get(card_id=Card.objects.get(card_id=card_id))
            form = InstrumentsUsedForm(data=request.POST)
            print(form.errors)
            if form.is_valid():
                new_card = form.save(commit=False)
                card = new_card
                card.inst_use_id = InstrumentUsed.objects.get(card_id=Card.objects.get(card_id=card_id)).inst_use_id
                card.card_id = Card.objects.get(card_id=card_id)
                card.save()
            return redirect(show_card, card_id)