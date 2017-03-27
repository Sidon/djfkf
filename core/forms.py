import json
from django import forms
from . import models as mdl

class RegCarForm(forms.ModelForm):

    dcars = {}
    list_cars = []
    for car in mdl.Car.objects.all():
        if car.brand.company_name in dcars:
            dcars[car.brand.company_name].append(car.name)
        else:
            dcars[car.brand.company_name] = [car.name]
        list_cars.append((car.name,car.name))

    brands = [str(brand) for brand in mdl.Brand.objects.all()]

    brand_select = forms.ChoiceField(choices=([(brand, brand) for brand in brands]))
    car_select = forms.ChoiceField(choices=(list_cars))

    brands = json.dumps(brands)
    cars = json.dumps(dcars)

    class Meta:
        model = mdl.Fleet
        fields = ('brand_select', 'car_select', 'description',)
