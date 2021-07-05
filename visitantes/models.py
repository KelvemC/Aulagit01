from django.db import models

class Visitante(models.Model):
    nome_completo = models.CharField(
        verbose_name='Nome completo',
        max_length=194,
    )

    cpf = models.CharField(
        verbose_name='CPF',
        max_length=11,
    )

    data_nascimento = models.DateField(
        verbose_name='Data de nascimento',
        auto_now=False,
        auto_now_add=False,
    )

    numero_casa = models.PositiveSmallIntegerField(
        verbose_name='Número da casa a ser visitada'
    )

    placa_veiculo = models.CharField(
        verbose_name='Placa do veículo',
        max_length=7,
        blank= True,
        null = True,
    )

    horario_chegada = models.DateTimeField(
        verbose_name='Horário de chegada da portaria',
        auto_now_add=True,
    )

    horario_saida = models.DateTimeField(
        verbose_name='Horário da saída',
        auto_now=False,
        blank=True,
        null= True,
    )

    horairo_autorizacao = models.DateTimeField(
        verbose_name='Horário da autorização de entrada',
        auto_now=False,
        blank=True,
        null = True,
    )

    morador_responsavel = models.CharField(
        verbose_name='Nome do morador responsável por autorizar a entrada do visitante',
        max_length=194,
        blank= True,
    )

    registrado = models.ForeignKey(
        'porteiros.Porteiro',
        verbose_name='Porteiro reponsável pelo registro',
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = 'Visitante'
        verbose_name_plural = 'Visitantes'
        db_table = 'visitantes'
    
    def __str__(self):
        return self.nome_completo