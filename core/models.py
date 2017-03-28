from django.db import models

class Brand(models.Model):
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name


class Car(models.Model):
    brand = models.ForeignKey(Brand)
    name = models.CharField(max_length=100)

    def brand_name(self):
        return self.brand.company_name

    def __str__(self):
        return self.name


class Fleet(models.Model):
    car = models.ForeignKey(Car)
    description = models.CharField(max_length=100)

    def car_name(self):
        return self.car.name

    def brand(self):
        return self.car.brand.company_name

    def __str__(self):
        return self.description
