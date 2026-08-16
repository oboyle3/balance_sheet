from django import forms
from .models import SIRRScenario


class SIRRScenarioForm(forms.Form):

    scenario = forms.ModelChoiceField(
        queryset=SIRRScenario.objects.all(),
        empty_label="Select a scenario"
    )