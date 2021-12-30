from rest_framework import serializers

from .models import RawMaterials, RMDemand, DemandedMaterials

# RAW Material Table Serializers
class RMCodeNumberSerializer(serializers.ModelSerializer):
    RMCode=serializers.CharField(max_length=100,required=True)
    class Meta:
        model=RawMaterials
        fields=['RMCode']

class MaterialNameSerializer(serializers.ModelSerializer):
    Material=serializers.CharField(max_length=100,required=True)
    class Meta:
        model=RawMaterials
        fields=['Material']


class RawMaterialInputSerializer(serializers.ModelSerializer):

    RMCode=serializers.CharField(max_length=100,required=True,write_only=True)
    Material = serializers.CharField(max_length=100, required=True, write_only=True)
    Units = serializers.CharField(max_length=100, required=True, write_only=True)
    Types = serializers.CharField(max_length=100, required=True,write_only=True)
    class Meta:
        model=RawMaterials
        fields=['RMCode','Material','Units','Types']

# DemandedMaterials Table Serializers
class DemandedMaterialsSerializer(serializers.ModelSerializer):
   class Meta:
        model=DemandedMaterials
        fields=['DNo']

# Input Serializer
class DemandedMaterialsInputSerializer(serializers.ModelSerializer):
    class Meta:
        model=DemandedMaterials
        fields='__all__'

# Demand Table Serilaizers
class DemandSerializer(serializers.ModelSerializer):
    DNo = serializers.CharField(max_length=20, help_text="DN01")
    class Meta:
        model=RMDemand
        fields=['DNo']

# Input Serializer
class DemandSerializerInput(serializers.ModelSerializer):
    DNo = serializers.CharField(max_length=20, help_text="DN01")
    Date = serializers.DateField(required=True)
    PlanNo = serializers.CharField(max_length=20)
    CancelledDates = serializers.DateField(required=True)
    PONo = serializers.CharField(max_length=20)
    material = DemandedMaterialsInputSerializer(many=True,write_only=True)
    class Meta:
        model = RMDemand
        fields = ['DNo','Date','PlanNo','CancelledDates','PONo','material']

    def create(self, validated_data):
        material_data = validated_data.pop('material')
        demand = RMDemand.objects.create(**validated_data)
        for materials_data in material_data:
            DemandedMaterials.objects.create(**materials_data)
        return demand


