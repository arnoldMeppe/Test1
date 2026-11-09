# views.py
from datetime import date

from django.http import HttpResponse

from docxtpl import DocxTemplate

from .forms import ContratForm

""" def generer_contrat(request):

    if request.method == "POST":
      form = ContratForm(request.POST)

      if form.is_valid():

       doc = DocxTemplate("templates_word/template.docx")
       context = {

         "nom": form.cleaned_data["nom"],

         "prenom": form.cleaned_data["prenom"],

         "date_naissance": form.cleaned_data["date_naissance"],

         "adresse": form.cleaned_data["adresse"],

         "date_generation": date.today()

        }

      doc.render(context)

      output_file = "contrat_genere.docx"

      doc.save(output_file)

      with open(output_file, "rb") as f:

       response = HttpResponse(

       f.read(),

 content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"

      )

       response["Content-Disposition"] = (

 'attachment; filename="contrat_genere.docx"'

      )

      return response

    else:
         form = ContratForm()
    return render(request, "contrat_form.html", {"form": form}) """



""" from django.http import HttpResponse

def generer_contrat(request):
    return HttpResponse("Application OK") """

""" 
from django.shortcuts import render
from .forms import ContratForm


def generer_contrat(request):
    form = ContratForm()

    return render(
        request,
        "Templates.html",
        {"form": form}
    ) """

from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContratForm
from docxtpl import DocxTemplate

""" doc = DocxTemplate("templates_word/Template.docx")

def generer_contract(request):

    if request.method == "POST":
        Doc.save("contrat_genere.docx")
        return HttpResponse("Document généré") 

    form = ContratForm()
    return render(request, "Templates.html", {"form": form})



def generer_contrat(request):

    if request.method == "POST":

        form = ContratForm(request.POST)

        if form.is_valid():

            doc = DocxTemplate("templates_word/Template.docx")

            context = {
                "model": form.cleaned_data["model"],
                "vatm": form.cleaned_data["vatm"],
                "vser": form.cleaned_data["vser"],
                "date": form.cleaned_data["date"],
                "nom": form.cleaned_data["nom"]
            }
            print(context)

            doc.render(context)
            doc.save("contrat_genere1.docx")

            return HttpResponse("Document généré")

    else:
        form = ContratForm()

    return render(request, "Templates.html", {"form": form}) 




from django.shortcuts import render
from .forms import ContratForm




def generer_contrat(request):

    if request.method == "POST":

        form = ContratForm(request.POST)

        if form.is_valid():

            data = form.cleaned_data

            print(data)

            return render(
                request,
                "success.html",
                {"data": data}
            )

    else:
        form = ContratForm()

    return render(
        request,
        "Templates.html",
        {"form": form}
    )

    if form.is_valid():

      for cle, valeur in form.cleaned_data.items():
         print(f"{cle} : {valeur}")


    """









# Importer les outils Django
from django.shortcuts import render
from django.http import HttpResponse

# Importer la bibliothèque pour remplir le Word
from docxtpl import DocxTemplate

# Importer os pour gérer le chemin du fichier
import os

# Importer les formulaires et modèles de ton projet
from .forms import ContratForm


def generer_pv(request):

    # Si le formulaire est envoyé
    if request.method == "POST":

        # Récupérer les données du formulaire
        form = ContratForm(request.POST)

        # Vérifier que le formulaire est valide
        if form.is_valid():

            # Récupérer les données nettoyées
            data = form.cleaned_data

            # Charger le template Word
            template = DocxTemplate(
                os.path.join(
                    os.path.dirname(__file__),
                    "Template.docx"
                )
            )

            # Préparer les données à envoyer au Word
            context = {

                # Informations générales
                "nom": data["nom_projet"],
                "date": data["date"].strftime("%d/%m/%Y"),

                # Versions
                "atm": data["atm"],
                "model": data["modele"],
                "perso": data["perso"],
                "vatm": data["version_atm"],
                "vser": data["version_serveur"],
                "objectif": data["objectif"],
                "materiel": data["materiel"],
                "responsable": data["responsable"],
                "reserves_p1_p2": data["p2_p1"],
                "reserves_p3": data["p3"],
                "tests": data["tests_effectues"],



                           # Case Patch Unitaire
                "patch_unitaire": "☒" if data["patch_unitaire"] else "☐",

    # Case Mise à jour
                "maj": "☒" if data["maj"] else "☐",

    # Case Service Pack
                "service_pack": "☒" if data["service_pack"] else "☐",

    # Case Installation complète
                "ic": "☒" if data["ic"] else "☐",

    # Case Template
                "template": "☒" if data["template"] else "☐",

    # Case Non-Régression Serveur
                "non_regression_serveur": (
                "☒" if data["non_regression_serveur"] else "☐"
    ),


            }

            # Injecter les données dans le template Word
            template.render(context)

            # Créer la réponse HTTP
            response = HttpResponse(
                content_type=(
                    "application/vnd.openxmlformats-officedocument."
                    "wordprocessingml.document"
                )
            )

            # Nom du fichier généré
            response["Content-Disposition"] = (
                'attachment; filename="PV_Recette.docx"'
            )

            # Enregistrer le Word dans la réponse
            template.save(response)

            # Retourner le fichier à l'utilisateur
            return response

    else:

        # Afficher un formulaire vide
        form = ContratForm()

    # Afficher la page du formulaire
    return render(
        request,
        "django.html",
        {"form": form}
    )