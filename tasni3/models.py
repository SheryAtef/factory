from django.db import models
from django.db.models import Sum

class Fabric(models.Model):
    code = models.CharField(max_length=10)
    material = models.CharField(max_length=100)
    COLOR_CHOICES = (
    ('Red', 'Red'),
    ('Green', 'Green'),
    ('Black', 'Black'),
    ('Blue', 'Blue'),
    ('Yellow', 'Yellow'),
    ('Black', 'Black'),
    ('Rose', 'Rose'),
    )
    color = models.CharField(max_length=15, choices=COLOR_CHOICES)
    quantity = models.FloatField()

    
    def publish(self):
         self.save()

    def __str__(self):
        return self.code

class Model(models.Model):
    modelNumber = models.IntegerField(primary_key=True)
    def __str__(self):
        return str(self.modelNumber)

    def publish(self):
         self.save()

class Kasa(models.Model):
    kasaNumber = models.IntegerField(primary_key=True)
    Date = models.DateField()
    RunCommand = models.FloatField()
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    #fabric= models.ForeignKey(Fabric, on_delete=models.CASCADE)
    #fabricQuanity = models.FloatField()
    #numberOfPieces= models.IntegerField()
    #PiecePrice = models.FloatField()
    def __str__(self):
        return str(self.kasaNumber)

    def publish(self):
         self.save()

class KasaFabrics(models.Model):
    fabric= models.ForeignKey(Fabric, on_delete=models.CASCADE)
    fabricQuanity = models.FloatField()
    kasa= models.ForeignKey(Kasa, on_delete=models.CASCADE)

    def publish(self):
         self.save()

'''class Worker(models.Model):
    workerName= models.CharField(max_length=100)
    numberOfPiecesTaken= models.IntegerField()
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    kasa = models.ForeignKey(Kasa, on_delete=models.CASCADE)
    numberOfPiecesBack = models.IntegerField()
    moneyTakenByTheWorker = models.FloatField()

    def publish(self):
         self.save()

    def __str__(self):
        return self.workerName
'''
