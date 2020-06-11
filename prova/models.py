from django.db import models


class Cargos(models.Model):
    nm_cargo = models.CharField(max_length=200)

    def __str__(self):
        return self.nm_cargo


class Pessoas(models.Model):
    id_cargo = models.ForeignKey(Cargos, on_delete=models.CASCADE)
    nm_pessoa = models.CharField(max_length=200)
    dt_admissao = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.nm_pessoa

