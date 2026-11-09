# forms.py
""" 
from django import forms
class ContratForm(forms.Form):

 vatm = forms.CharField(max_length=100)

 model = forms.CharField(max_length=100)

 vser = forms.CharField(max_length=100)

 nom = forms.CharField(max_length=100)

 date = forms.DateField(

 widget=forms.DateInput(attrs={"type": "date"})

 )

adresse = forms.CharField(widget=forms.Textarea) """

from django import forms


class ContratForm(forms.Form):

    # Informations générales
    nom_projet = forms.CharField(
        label="Nom projet",
        max_length=200
    )

    environnement = forms.ChoiceField(
        label="Environnement",
        choices=[
            ("RECETTE", "RECETTE"),
            ("PREPROD", "PREPROD"),
            ("PROD", "PRODUCTION"),
        ]
    )

    version_serveur = forms.CharField(
        label="Version serveur",
        required=False
    )

    version_atm = forms.CharField(
        label="Version ATM",
        required=False
    )

    date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"})
    )

    atm = forms.CharField(
        label="ATM",
        required=False
    )

    constructeur = forms.CharField(
        label="Constructeur",
        required=False
    )

    modele = forms.CharField(
        label="Modèle",
        required=False
    )

    responsable = forms.CharField(
        label="Responsable",
        required=False
    )

    perso = forms.CharField(
        label="Perso",
        required=False
    )

    # Matériel et tests
    materiel_disponible = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 4}),
        required=False
    )

    tests_effectues = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 6})
    )

    reserves_p1_p2 = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 4}),
        required=False
    )

    reserves_p3 = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 4}),
        required=False
    )

    # Description
    patch_unitaire = forms.BooleanField(required=False)
    template = forms.BooleanField(required=False)
    service_pack = forms.BooleanField(required=False)

    maj = forms.BooleanField(required=False)
    ic = forms.BooleanField(required=False)
    non_regression_serveur = forms.BooleanField(required=False)

    # Conclusion
    type_reception = forms.ChoiceField(
        choices=[
            ("provisoire", "Provisoire"),
            ("definitive", "Définitive"),
        ],
        widget=forms.RadioSelect
    )

    type_pv = forms.ChoiceField(
            choices=[
                ("avec_reserve", "Avec réserve"),
                ("sans_reserve", "Sans réserve"),
            ],
            widget=forms.RadioSelect
        )
    conclusion = forms.ChoiceField(
        choices=[
            ("acceptee", "Acceptée"),
            ("refusee", "Refusée"),
            
        ],
        
        widget=forms.RadioSelect
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            if not isinstance(field.widget,
                              (forms.CheckboxInput,
                               forms.RadioSelect)):
                field.widget.attrs.update({
                    "class": "form-control"
                })