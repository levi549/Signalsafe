from django.db import models
import uuid
from django.db import models


class User(models.Model):
    id = models.UUIDField(primary_key=True)
    email = models.EmailField(max_length=255)
    nome = models.CharField(max_length=255)
    is_admin = models.BooleanField()

    class Meta:
        managed = False
        db_table = "users"

    def __str__(self):
        return self.email


class Estabelecimento(models.Model):
    id = models.UUIDField(primary_key=True)
    nome = models.CharField(max_length=255)
    cep = models.TextField()
    id_user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        db_column="id_user",
        related_name="estabelecimentos",
    )

    class Meta:
        managed = False
        db_table = "estabelecimentos"

    def __str__(self):
        return self.nome


class Sala(models.Model):
    id = models.UUIDField(primary_key=True)
    nome = models.CharField(max_length=255)
    id_estabe = models.ForeignKey(
        Estabelecimento,
        on_delete=models.PROTECT,
        db_column="id_estabe",
        related_name="salas",
    )

    class Meta:
        managed = False
        db_table = "sala"

    def __str__(self):
        return self.nome


class Jammer(models.Model):
    id = models.UUIDField(primary_key=True)
    status = models.BooleanField()
    id_sala = models.ForeignKey(
        Sala,
        on_delete=models.PROTECT,
        db_column="id_sala",
        related_name="jammers",
    )

    class Meta:
        managed = False
        db_table = "jammer"


class DimData(models.Model):
    id_data = models.IntegerField(primary_key=True)
    data_completa = models.DateField()
    ano = models.IntegerField()
    mes = models.IntegerField()
    nome_mes = models.CharField(max_length=100)
    dia = models.IntegerField()
    nome_dia_semana = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "dim_data"

    def __str__(self):
        return str(self.data_completa)


class DimTempo(models.Model):
    id_tempo = models.IntegerField(primary_key=True)
    hora = models.IntegerField()
    minuto = models.IntegerField()
    turno = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = "dim_tempo"

    def __str__(self):
        return f"{self.hora:02d}:{self.minuto:02d}"


class Fatos(models.Model):
    id_fatos = models.UUIDField(primary_key=True)
    id_jammer = models.ForeignKey(
        Jammer,
        on_delete=models.PROTECT,
        db_column="id_jammer",
        related_name="fatos",
    )
    id_data = models.ForeignKey(
        DimData,
        on_delete=models.PROTECT,
        db_column="id_data",
        related_name="fatos",
    )
    id_tempo = models.ForeignKey(
        DimTempo,
        on_delete=models.PROTECT,
        db_column="id_tempo",
        related_name="fatos",
    )
    tipo_sinal = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "fatos"