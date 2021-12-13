from django.db import models


# Create your models here.


# A primitive extension of the standard User table from Django lib
class RawMaterials(models.Model):             #2 Api's
    ChoiceRole = (
        ("Leather", "Leather"),
        ("Paint", "Paint"),
        ("Iron", "Iron"),
        ("Plastic", "Plastic"),
    )
    RMCode = models.CharField(unique=True,max_length=20,null=False,help_text="RM01")
    Material = models.CharField(unique=True,max_length=20,null=False)
    Units = models.CharField(max_length=20, null=False)
    Types = models.CharField(default='Accounts', max_length=50, choices=ChoiceRole)

    def __str__(self):
        return str('%s %s' % (self.RMCode, self.Material))


class RMDemand(models.Model):              #1 Api   input in all fields
    DNo = models.CharField(unique=True, max_length=20, null=False, help_text="DN01")
    Date = models.DateField(null=False)    #2 Api   get Api , Dno given and whole data is return from table
    PlanNo = models.CharField(unique=True, max_length=20, null=False, help_text="PLN01")
    CancelledDates = models.DateField(null=False)
    PONo = models.CharField(unique=True, max_length=20, null=False, help_text="PON01")

    def __str__(self):
        return str('%s %s %s' % (self.DNo, self.PlanNo, self.PONo))


class DemandedMaterials(models.Model):   # 1 Api to input data
    ChoiceRole = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
    )
    DemandedQuantity = models.CharField(max_length=200, null=False)
    CurrentStock = models.CharField(max_length=200, null=False)
    status = models.CharField(max_length=200,null=False)
    Priority = models.CharField(default='1',max_length=50,choices=ChoiceRole)
    DNo =  models.ForeignKey(RMDemand, to_field = 'DNo', on_delete=models.CASCADE)
    RMCode = models.ForeignKey(RawMaterials, to_field = 'RMCode', on_delete=models.CASCADE)

    def __str__(self):
        return str('%s %s %s' % (self.DemandedQuantity, self.DNo, self.Priority))