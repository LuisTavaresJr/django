from django.db import models
from django.urls import reverse
from django.conf import settings

class CourseManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) |
            models.Q(description__icontains=query)
        )

class Course(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição Simples', blank=True
                                   ) # blank=True diz que o campo nao é obrigatorio
    about = models.TextField('Sobre o Curso', blank=True)
    start_date = models.DateField(
        'Data de Início', null=True, blank=True
    ) #null a nivel de banco de dados ele pode ser nulabo
    image = models.ImageField(upload_to='courses/images', verbose_name='Imagens',
                              null=True, blank=True
                              ) # image precisa do MEDIA_ROOT no settings é onde os arquivos vão ficar
    # objetos do tipo imagens precisa da biblioteca Pil ou Pillow
    created_at = models.DateTimeField(
        'Criado em', auto_now_add=True
    ) #quando for criado um curso ele vai ser adicionado a data
    updated_at = models.DateTimeField(
        'Atualizado em', auto_now=True
    ) # auto_now toda vez que for salvo ele vai ser atualizado a data

    objects = CourseManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/cursos/{self.slug}'

    # def get_absolute_url(self):
    #     return reverse('details', args=[self.slug])

    class Meta(): # classe meta é do model, fazemos algumas alteraçoes
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['name'] # alteramos a ordem dos cursos pra ordenar por ordem crescenta

# model de inscricoes dos cursos
class Enrollment(models.Model):

    STATUS_CHOICES = (
        (0, 'Pendente'),
        (1, 'Aprovado'),
        (2, 'Cancelado'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='Usuário', related_name='enrollments', on_delete=models.CASCADE
    )
    course = models.ForeignKey(
        Course, verbose_name='Curso', related_name='enrollments', on_delete=models.CASCADE
    )
    status = models.IntegerField(
        'Situação', choices=STATUS_CHOICES, default=0, blank=True
    )
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def active(self): # ativação automatica, assim q se inscrever status fica aprovado
        self.status = 1
        self.save()

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
        unique_together = (('user', 'course'),)# para que nao tenha duplicidade nas iscricoes dos cursos