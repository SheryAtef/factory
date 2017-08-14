from django.contrib import admin
from .models import Kasa
from .models import KasaFabrics
from .models import Model
from .models import Fabric
from django.db.models import Sum
from django.db import transaction

class FabricAdmin(admin.ModelAdmin):

    def update_quantity(self,obj):
        #obj = Fabric.objects.last()
        total = 0.0;
        if Fabric.objects.filter(code=obj.code, color=obj.color, material=obj.material ).count() > 1:
            for row1 in Fabric.objects.filter(code=obj.code,  color=obj.color, material=obj.material):
                total= total + row1.quantity

            for row in Fabric.objects.all():
                if Fabric.objects.filter(code=row.code, color=row.color, material=row.material ).count() > 1:
                   row.delete()

            Fabric.objects.filter(code=obj.code,  color=obj.color, material=obj.material).update(quantity= total)
        return

    #transaction.on_commit(update_quantity)
    list_display= ('code', 'material', 'color', 'quantity','update_quantity')
    #update_quantity(obj)
admin.site.register(Fabric,FabricAdmin)

class KasaAdmin(admin.ModelAdmin):
    #def get_ModelNumber(self, obj):
    #    return obj.model.modelNumber
    #def updateFabrics(self,obj)
    list_display = ('kasaNumber','RunCommand','Date', 'model' ,)
admin.site.register(Kasa, KasaAdmin)

class KasaFabricsAdmin(admin.ModelAdmin):

    global_NumberOfTimes=1

    def get_Net(self,obj):
        global global_NumberOfTimes
        #print(KasaFabrics.objects.all().count())
        #print("aho number of times")
        print "numberofTimes aho" , self.global_NumberOfTimes
        if KasaFabrics.objects.all().count() >= self.global_NumberOfTimes:
           taken = obj.fabricQuanity
           print "taken aho",taken
           net = 0.0
           total=0.0
           instance=Fabric.objects.filter(code=obj.fabric.code, material=obj.fabric.material,color= obj.fabric.color).values('quantity')[0]
           print(instance)
           total = instance.get('quantity')
           print (total)
           print(taken)
           net = total-taken
           Fabric.objects.filter(code=obj.fabric.code, material=obj.fabric.material,color= obj.fabric.color).update(quantity=net)
           self.global_NumberOfTimes=self.global_NumberOfTimes+1
           print("shooof")
           print (self.global_NumberOfTimes)
        return "Done"
        print (global_NumberOfTimes)
    list_display = ('fabric','fabricQuanity','kasa','get_Net')
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

'''def updateFabrics(self, obj):
    codeAdded = obj.fabric.code
    #quantity = obj.fabricQuanity
    fab = Fabric.objects.filter(code = codeAdded)
    fab.quantity=fab.quantity - obj.fabricQuanity
    fab.save()
    return fab.quantity

    def get_TotalQuantity(self,obj):
        qs = self.model._default_manager.filter(code=obj.code, material=obj.material,color=obj.color)
        quantity_agg = qs.aggregate(Sum('quantity'))
         return qs.update(quantity=quantity_agg)

           def deleteRepeated(self,obj):
             for row in Fabric.objects.all():
                 if Fabric.objects.filter(code=row.code, color=row.color, material=row.material ).count() > 1:
                    row.delete()
             return "Done"'''
# Register your models here.
