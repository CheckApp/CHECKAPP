from django.db import models


class Categoria(models.Model):
    nome_cat = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_cat



class Assinatura(models.Model):
    assinatura = models.CharField(max_length=50)

    def __str__(self):
        return self.assinatura



class Estado(models.Model):
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.estado



class Cidade(models.Model):
    cidade = models.CharField(max_length=50)

    def __str__(self):
        return self.cidade



class Bairro(models.Model):
    bairro = models.CharField(max_length=50)

    def __str__(self):
        return self.bairro



class SistemaPDV(models.Model):
    sistemaPDV = models.CharField(max_length=50)

    def __str__(self):
        return self.sistemaPDV



class Consultor(models.Model):
    consultor = models.CharField(max_length=50)

    def __str__(self):
        return self.consultor



class Bandeira(models.Model):
    bandeira = models.CharField(max_length=50)

    def __str__(self):
        return self.bandeira



class Rede(models.Model):
    rede = models.CharField(max_length=50)

    def __str__(self):
        return self.rede

class Uso(models.Model):
    uso = models.CharField(max_length=50)

    def __str__(self):
        return self.uso

class Perfil(models.Model):
    perfil = models.CharField(max_length=50)

    def __str__(self):
        return self.perfil


