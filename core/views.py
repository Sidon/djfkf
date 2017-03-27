from django.shortcuts import render
from .forms import RegCarForm
from .models import Car, Fleet

# Create your views here.

def regcar(request):
    if request.method == 'POST':
        car_form = RegCarForm(data=request.POST)

        if car_form.is_valid():
            cdata = car_form.cleaned_data.get
            car_selected = Car.objects.filter(name=cdata('car_select'))
            reg1 = Fleet(car_id=car_selected[0].id, description=cdata('description'))
            reg1.save()
        else:
            print ('Invalid')

    else:
        car_form = RegCarForm()
    return render(request, 'core/regcar.html', {'car_form': car_form})


