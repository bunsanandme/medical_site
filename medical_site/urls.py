from django.contrib import admin
from django.urls import path, include
from medical import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path("add/", views.add_pacient, name="add"),
    path("pacient/<int:pacient_id>", views.show_pacient, name="pacient"),
    path("pacient/delete/<int:pacient_id>", views.action_with_pacient, name="delete"),
    path("pacient/all", views.show_all_pacients, name="show_all"),
    path("card/<int:card_id>", views.show_card, name="show_card"),
    path("pacient/edit/<int:pacient_id>", views.action_with_pacient, name="edit"),
    path("pacient/", views.search_pacient, name="search"),
    path("card/create/<int:pacient_id>", views.add_new_card, name="add_card"),
    path("card/edit/<int:card_id>", views.edit_card, name="edit_card"),
    path("mh/edit/<int:card_id>", views.edit_medical_history, name="edit_medical_history"),
    path("sh/edit/<int:card_id>", views.edit_surgical_history, name="edit_surgical_history"),
    path("gp/edit/<int:card_id>", views.edit_gastro_procedure, name="edit_gastro_procedure"),
    path("up/edit/<int:card_id>", views.edit_uro_procedure, name="edit_uro_procedure"),
    path("spd/edit/<int:card_id>", views.edit_spd, name="edit_spd"),
    path("ral/edit/<int:card_id>", views.edit_ral, name="edit_ral"),
    path("tl/edit/<int:card_id>", views.edit_tl, name="edit_tl"),
]

urlpatterns += [ 
    path('', include('django.contrib.auth.urls')),
]