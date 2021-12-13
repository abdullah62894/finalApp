from django.contrib import admin
from .models import RMDemand,RawMaterials,DemandedMaterials
# Register your models here.

admin.site.register(RMDemand)
admin.site.register(RawMaterials)
admin.site.register(DemandedMaterials)
