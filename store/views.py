from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import RawMaterials, RMDemand, DemandedMaterials
from .serializers import RMCodeNumberSerializer, MaterialNameSerializer, \
    RawMaterialInputSerializer, DemandedMaterialsSerializer,DemandedMaterialsInputSerializer,\
    DemandSerializer, DemandSerializerInput

# GET APIS FOR Raw Material Table
class RMCodeslist(APIView):
    serializer_class = RMCodeNumberSerializer

    def get(self, request):
        RMcodelist = RawMaterials.objects.all()
        serializer = RMCodeNumberSerializer(RMcodelist, many=True)
        return Response(serializer.data)

class MaterialNameslist(APIView):
    serializer_class = MaterialNameSerializer

    def get(self, request):
        materiallist = RawMaterials.objects.all()
        serializer = MaterialNameSerializer(materiallist, many=True)
        return Response(serializer.data)

class GetRMbyCodeNo(APIView):
    serializer_class = RMCodeNumberSerializer

    def get(self, request, RMCode):
        checkInDB = RawMaterials.objects.filter(RMCode=RMCode)
        if checkInDB:
            dataAgainstRMCode = RawMaterials.objects.filter(RMCode=RMCode).values("Material", "Units", "Types")
            return Response(dataAgainstRMCode)
        else:
            return Response("Wrong Rmcode Number")

class GetRMbyName(APIView):
    serializer_class = MaterialNameSerializer

    def get(self, request, Material):
        checkInDB = RawMaterials.objects.filter(Material=Material)
        if checkInDB:
            dataAgainstMaterialName = RawMaterials.objects.filter(Material=Material).values("Material", "Units", "Types")
            return Response(dataAgainstMaterialName)
        else:
            return Response("Wrong Material Name")

# Input APIS FOR Raw Material Table
class InsertRawMaterials(APIView):
    serializer_class = RawMaterialInputSerializer

    def post(self, request):
        dataa = {
            "RmCode": request.data['RMCode'],
            "Material": request.data['Material'],
            "Types": request.data['Types'],
        }
        serializer = RawMaterialInputSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(dataa)

        else:
            return Response("Serializer not valid")

        return Response("Check")

# GET APIS FOR Demand Table
class GetDemands(APIView):
    serializer_class = DemandSerializer

    def get(self, request, DNo):
        checkInDB = RMDemand.objects.filter(DNo=DNo)
        if checkInDB:
            dataAgainstDNo = RMDemand.objects.filter(DNo=DNo).values("Date", "PlanNo", "CancelledDates", "PONo")
            return Response(dataAgainstDNo)
        else:
            return Response("Wrong DNo ")

class GetLatestDemanded(APIView):
    serializer_class = DemandedMaterialsSerializer

    def get(self, request):
        latestDemand = RMDemand.objects.latest('DNo')
        return Response(latestDemand.DNo)

# Input APIS FOR Demand Table
class InsertDemand(APIView):
    serializer_class = DemandSerializerInput

    def post(self, request):
        serializer = DemandSerializerInput(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors)

# GET APIS FOR Demanded Item Table
class GetDemandedMaterials(APIView):
    serializer_class = DemandedMaterialsSerializer

    def get(self, request, DNo):
        checkInDB = DemandedMaterials.objects.filter(DNo=DNo)
        if checkInDB:
            dataAgainstDNoinDemandMaterial = DemandedMaterials.objects.filter(DNo=DNo).values("DemandedQuantity",
                                                                                              "CurrentStock", "status",
                                                                                              "Priority", "RMCode")
            return Response(dataAgainstDNoinDemandMaterial)
        else:
            return Response("Wrong DNo ")

# Input APIS FOR Demanded Item Table
class InsertDemandedMaterials(APIView):
    serializer_class = DemandedMaterialsInputSerializer

    def post(self, request):
        data = {
            "DemandedQuantity": request.data['DemandedQuantity'],
            "CurrentStock": request.data['CurrentStock'],
            "status": request.data['status'],
            "Priority": request.data['Priority'],
            "DNo": request.data['DNo'],
            "RMCode": request.data['RMCode']
        }
        serializer = DemandedMaterialsInputSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data)

        else:
            return Response("Serializer not valid")

        return Response("Check")

