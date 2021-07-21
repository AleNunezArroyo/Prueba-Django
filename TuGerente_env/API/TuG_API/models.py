from django.db import models

# Create your models here.
class Person(models.Model):
    state = (
        ('Pendiente', 'Pendiente'),
        ('Pagado', 'Pagado'),
        ('Eliminado', 'Eliminado'),
    )
    pay = (
        ('Tarjeta', 'Tarjeta'),
        ('Transferencia', 'Transferencia'),
        ('Efectivo', 'Efectivo'),
    )
    place = (
        ('1A', 'Piso 1, cuarto A'),
        ('1B', 'Piso 1, cuarto B'),
        ('1C', 'Piso 1, cuarto C'),
        ('1D', 'Piso 1, cuarto D'),
        ('2A', 'Piso 2, cuarto A'),
        ('2B', 'Piso 2, cuarto B'),
        ('2C', 'Piso 2, cuarto C'),
        ('2D', 'Piso 2, cuarto D'),      
    )
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.CharField(max_length=30)
    data_start = models.DateTimeField('Inicio de reserva')
    data_end = models.DateTimeField('Fin de reserva')
    state_place = models.CharField(max_length=10, choices=state, default='none')
    payment_method = models.CharField(max_length=15, choices=pay, default='none')
    nit = models.IntegerField(default=0)
    placement = models.CharField(max_length=30, choices=place, default='none')
    payment = models.IntegerField(default=0)

