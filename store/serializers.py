from rest_framework import serializers

from .models import RawMaterials, RMDemand, DemandedMaterials


class RawMaterialSerializerRMCodeNumber(serializers.ModelSerializer):
    RMCode=serializers.CharField(max_length=100,required=True)
    class Meta:
        model=RawMaterials
        fields=['RMCode']

class RawMaterialSerializerMaterialName(serializers.ModelSerializer):
    Material=serializers.CharField(max_length=100,required=True)
    class Meta:
        model=RawMaterials
        fields=['Material']


class RawMaterialSerializerInput(serializers.ModelSerializer):

    RMCode=serializers.CharField(max_length=100,required=True,write_only=True)
    Material = serializers.CharField(max_length=100, required=True, write_only=True)
    Units = serializers.CharField(max_length=100, required=True, write_only=True)
    Types = serializers.CharField(max_length=100, required=True,write_only=True)
    class Meta:
        model=RawMaterials
        fields=['RMCode','Material','Units','Types']

class RMDemandSerializerInput(serializers.ModelSerializer):
    DNo = serializers.CharField(max_length=20, help_text="DN01")
    Date = serializers.DateField(required=True)
    PlanNo = serializers.CharField(max_length=20)
    CancelledDates = serializers.DateField(required=True)
    PONo = serializers.CharField(max_length=20)

    class Meta:
        model=RMDemand
        fields='__all__'

class RMDemandSerializerDNo(serializers.ModelSerializer):
    DNo = serializers.CharField(max_length=20, help_text="DN01")
    class Meta:
        model=RMDemand
        fields=['DNo']

#-------------------------------------------------


class DemandedMaterialsSerializerInput(serializers.ModelSerializer):
    DemandedQuantity = serializers.CharField(max_length=200)
    CurrentStock = serializers.CharField(max_length=200)
    status = serializers.CharField(max_length=200)
    Priority = serializers.CharField(max_length=50)
    #DNo = serializers.ForeignKey(RMDemand, to_field='DNo', on_delete=serializers.CASCADE)
    #RMCode = serializers.ForeignKey(RawMaterials, to_field='RMCode', on_delete=serializers.CASCADE)

    class Meta:
        model=DemandedMaterials
        fields='__all__'

class DemandedMaterialsDNoSerializerInput(serializers.ModelSerializer):
   class Meta:
        model=DemandedMaterials
        fields=['DNo']