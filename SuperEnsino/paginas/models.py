from django.db import models

# Create your models here.

class Disciplina(models.Model):
    nome = models.CharField(max_length=100, null=False, default='Informe a disciplina', verbose_name='Disciplina')
    
    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'

    def __str__(self):
        return self.nome

class Serie(models.Model):
    serie = models.CharField(max_length=100,default=None,help_text='Por favor, informe a série')

    class Meta:
        verbose_name = 'Serie'
        verbose_name_plural = 'Series'
    
    def __str__(self):
        return self.serie

class Questionario(models.Model):
    BIMESTRES = (
        ('1','1º bimestre'),
        ('2','2º bimestre'),
        ('3','3º bimestre'),
        ('4','4º bimestre'),
    )
    
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)  
    serie = models.ForeignKey(Serie, on_delete=models.DO_NOTHING) 
    bimestre = models.TextField(default=None,help_text='Por favor, informe o bimestre', choices=BIMESTRES)
    is_recuperacao = models.BooleanField(default=False, verbose_name='Recuperação?')

    class Meta:
        verbose_name = 'Questionario'
        verbose_name_plural = 'Questionarios'

    def __str__(self):
        return f'{self.disciplina.nome} | {self.serie} | {self.bimestre} bimestre {"| (Recuperação)" if self.is_recuperacao else ""}'

class Pergunta(models.Model):
    questionario = models.ForeignKey(Questionario, on_delete=models.CASCADE)
    enunciado = models.TextField(null=False, help_text='Por favor, informe o enunciado')

    class Meta:
        verbose_name = 'Pergunta'
        verbose_name_plural = 'Perguntas'

    def __str__(self):
        return f'Questionario {self.questionario.id} - {self.enunciado}'

class Alternativa(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)

    alternativa_a = models.TextField(null=False, verbose_name='Alternativa A',help_text='Por favor, informe a alternativa')
    alternativa_b = models.TextField(null=False, verbose_name='Alternativa B',help_text='Por favor, informe a alternativa')
    alternativa_c = models.TextField(null=False, verbose_name='Alternativa C',help_text='Por favor, informe a alternativa')
    alternativa_d = models.TextField(null=False, verbose_name='Alternativa D',help_text='Por favor, informe a alternativa')
    
    RESPOSTAS = (
        (None,''), 
        ('a','Resposta A'), 
        ('b','Resposta B'), 
        ('c','Resposta C'), 
        ('d','Resposta D')
        )
    alternativa_correta = models.TextField(default=None, verbose_name='Alternativa correta:', choices=RESPOSTAS, null=False) 

    class Meta:
        verbose_name = 'Alternativa'
        verbose_name_plural = 'Alternativas'

    def verifica_resposta(self,valor):
        return valor == self.alternativa_correta

    def __str__(self):
        if len(self.pergunta.enunciado) > 15:
            if len(self.alternativa_correta) > 15:
                return f'id {self.id}  -  Resposta correta: {self.alternativa_correta[:15]} ... - {self.pergunta.enunciado[:15]} ...'
            else:
                return f'id {self.id}  -  Resposta correta: {self.alternativa_correta} - {self.pergunta.enunciado[:15]} ...'
        else:
            if len(self.alternativa_correta) > 15:
                return f'id {self.id}  -  Resposta correta: {self.alternativa_correta[:15]} ... - {self.pergunta.enunciado}'
            else:
                return f'id {self.id}  -  Resposta correta: {self.alternativa_correta} - {self.pergunta.enunciado} '

class Aluno(models.Model):
    nome = models.CharField(max_length=150, null=False, help_text='Nome aluno:')
    serie = models.ForeignKey(Serie, on_delete=models.DO_NOTHING) 

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

    def __str__(self):
        return f'{self.id} | {self.nome} - {self.serie.serie}'

class Resposta(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    ALTERNATIVAS = (
        ('a','Alternativa A'), 
        ('b','Alternativa B'), 
        ('c','Alternativa C'), 
        ('d','Alternativa D')
        )
    valor = models.TextField(default=None, verbose_name='Alternativa correta:', choices=ALTERNATIVAS, null=False) 
    is_correta = models.BooleanField(default=None)

    class Meta:
        verbose_name = 'Resposta'
        verbose_name_plural = 'Respostas'

    def __str__(self):
        return f'aluno {self.aluno.id} | pergunta {self.pergunta.id} | valor {self.valor} | is_correta {self.is_correta}'
