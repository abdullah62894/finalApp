from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import RawMaterials, RMDemand, DemandedMaterials
from .serializers import RawMaterialSerializerRMCodeNumber, RawMaterialSerializerMaterialName, \
    RawMaterialSerializerInput, DemandedMaterialsSerializerInput, DemandedMaterialsDNoSerializerInput
from .serializers import RMDemandSerializerInput, RMDemandSerializerDNo


class StoreView(APIView):
    serializer_class = RawMaterialSerializerRMCodeNumber

    def post(self, request):
        data = request.data
        serializer = RawMaterialSerializerRMCodeNumber(data=request.data)
        RMCode = data.get('RMCode', None)
        # print("RMCOde ",RMCode)
        checkInDB = RawMaterials.objects.get(RMCode=RMCode)
        # print("Check ",checkInDB)
        if serializer.is_valid():
            if checkInDB:
                dataAgainstRMCode = RawMaterials.objects.filter(RMCode=RMCode).values("Material", "Units", "Types")
                return Response(dataAgainstRMCode)
            else:
                return Response("Wrong Rmcode Number")
        else:
            return Response("Serializer not valid")

        return Response("account not found One")


class MaterialName(APIView):
    serializer_class = RawMaterialSerializerMaterialName

    def post(self, request):
        data = request.data
        serializer = RawMaterialSerializerMaterialName(data=request.data)
        MaterialName = data.get('Material', None)
        checkInDB = RawMaterials.objects.get(Material=MaterialName)
        if serializer.is_valid():
            dataAgainstRMCode = RawMaterials.objects.filter(Material=MaterialName).values("RMCode", "Units", "Types")
            return Response(dataAgainstRMCode)
        # else:
        #         return Response("Wrong Material Name")
        else:
            return Response("Serializer not valid")

        return Response("Check")


class RMCodeInputAPI(APIView):
    serializer_class = RawMaterialSerializerInput

    def post(self, request):
        dataa = {
            "RmCode": request.data['RMCode'],
            "Material": request.data['Material'],
            "Types": request.data['Types'],
        }
        serializer = RawMaterialSerializerInput(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(dataa)

        else:
            return Response("Serializer not valid")

        return Response("Check")


class RMDemandInputAPI(APIView):
    serializer_class = RMDemandSerializerInput

    def post(self, request):
        data = {
            "DNo": request.data['DNo'],
            "Date": request.data['Date'],
            "PlanNo": request.data['PlanNo'],
            "CancelledDates": request.data['CancelledDates'],
            "PONo": request.data['PONo']
        }
        serializer = RMDemandSerializerInput(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data)

        else:
            return Response("Serializer not valid")

        return Response("Check")


class RMDemandDNoAPI(APIView):
    serializer_class = RMDemandSerializerDNo

    def post(self, request):
        data = request.data
        serializer = RMDemandSerializerDNo(data=request.data)
        DNo = data.get('DNo', None)
        if serializer.is_valid():
            dataAgainstDNo = RMDemand.objects.filter(DNo=DNo).values("Date", "PlanNo", "CancelledDates", "PONo")
            return Response(dataAgainstDNo)

        else:
            return Response("Serializer not valid")

        return Response("Check API")


# --------------------------------------------
class DemandedMaterialInputAPI(APIView):
    serializer_class = DemandedMaterialsSerializerInput

    def post(self, request):
        data = {
            "DemandedQuantity": request.data['DemandedQuantity'],
            "CurrentStock": request.data['CurrentStock'],
            "status": request.data['status'],
            "Priority": request.data['Priority'],
            "DNo": request.data['DNo'],
            "RMCode": request.data['RMCode']
        }
        serializer = DemandedMaterialsSerializerInput(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data)

        else:
            return Response("Serializer not valid")

        return Response("Check")


class DemandedMaterialDNoAPI(APIView):
    serializer_class = DemandedMaterialsDNoSerializerInput

    def post(self, request):
        data = request.data
        serializer = DemandedMaterialsDNoSerializerInput(data=request.data)
        DNo = data.get('DNo', None)
        if serializer.is_valid():
            dataAgainstDNoinDemandMaterial = DemandedMaterials.objects.filter(DNo=DNo).values("DemandedQuantity",
                                                                                              "CurrentStock", "status",
                                                                                              "Priority", "RMCode")
            return Response(dataAgainstDNoinDemandMaterial)
            return Response(data)

        else:
            return Response("Serializer not valid")

        return Response("Check")
