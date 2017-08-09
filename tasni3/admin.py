from django.contrib import admin
from .models import Kasa
from .models import KasaFabrics
from .models import Model
from .models import Fabric


class FabricAdmin(admin.ModelAdmin):
    list_display= ('code', 'material', 'color', 'quantity',)
admin.site.register(Fabric,FabricAdmin)

class KasaAdmin(admin.ModelAdmin):
    #def get_ModelNumber(self, obj):
    #    return obj.model.modelNumber

    list_display = ('kasaNumber','RunCommand','Date', 'model' ,)
admin.site.register(Kasa, KasaAdmin)

class KasaFabricsAdmin(admin.ModelAdmin):

    def updateFabrics(self, obj):
        codeAdded = obj.fabric.code
        #quantity = obj.fabricQuanity
        fab = Fabric.objects.filter(code = codeAdded)
        fab.quantity=fab.quantity - obj.fabricQuanity
        fab.save()
        return fab.quantity

    list_display = ('fabric','fabricQuanity','kasa','updateFabrics',)
admin.site.register(KasaFabrics,KasaFabricsAdmin)

#class ModelAdmin(admin.ModelAdmin):
#    list_display = ('modelNumber',)
admin.site.register(Model)

'''
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('workerName','numberOfPiecesTaken','model','kasa', 'numberOfPiecesBack','moneyTakenByTheWorker',)
    #list_filter = ('person', ('lastAttendance',DateRangeFilter) ,)
admin.site.register(Worker,WorkerAdmin)
'''
# Register your models here.
