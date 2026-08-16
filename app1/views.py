from django.shortcuts import render
from.models import MortgagePool
from .forms import SIRRScenarioForm

from .forms import SIRRScenarioForm
from .engine.sirr import calculate_sirr

# Create your views here.
def home(request):
    pools = MortgagePool.objects.all()
    return render(request,"home.html")



def eodrisk(request):
    return render(request,"eodrisk.html")

####



def sirr(request):

    result = None
    scenario = None

    if request.method == "POST":

        form = SIRRScenarioForm(request.POST)

        if form.is_valid():

            scenario = form.cleaned_data["scenario"]

            coupon = scenario.coupon_rate
            funding = scenario.funding_cost
            credit_loss = scenario.credit_loss
            servicing = scenario.servicing_cost

            result = coupon - funding - credit_loss - servicing

    else:

        form = SIRRScenarioForm()

    return render(
        request,
        "sirr.html",
        {
            "form": form,
            "result": result,
            "scenario": scenario,
        }
    )