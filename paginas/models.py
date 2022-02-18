from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):

    name = models.CharField(max_length=50, help_text="Digite seu nome completo")
    identification = models.CharField(max_length=11, help_text="Informe seu cpf")
    state = models.CharField(max_length=100, help_text="Informe seu estado")
    city = models.CharField(max_length=100, help_text="Informe sua cidade")

    def __str__(self):
        return self.name + ' - ' + str(self.identification) + ' - ' + str(self.state) + ' - ' + str(self.city)

class Operator(models.Model):

    name = models.CharField(max_length=50, help_text="Digite o nome completo do operador")
    identification = models.CharField(max_length=11, help_text='Informe o CPF do operador')
    area = models.CharField(max_length=100, help_text="Informe a área do operador")
    department = models.CharField(max_length=100, help_text="Informe o departamento do operador")
    rank = models.CharField(max_length=100, help_text="Informe o cargo do operador")
    payment = models.CharField(max_length=100, help_text="Informe o salário do operador")
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name + ' - ' + str(self.identification) + ' - ' + str(self.area) + ' - ' + str(self.department) + ' - ' + str(self.rank) + ' - ' + str(self.payment)

class Service(models.Model):

    name = models.CharField(max_length=50, help_text="Digite o nome completo do operador")
    stage = models.CharField(max_length=50, help_text='Informe o CPF do operador')
    level = models.CharField(max_length=100, help_text="Informe a área do operador")
    price = models.CharField(max_length=100, help_text="Informe o departamento do operador")
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name + ' - ' + str(self.stage) + ' - ' + str(self.level) + ' - ' + str(self.price)
        
