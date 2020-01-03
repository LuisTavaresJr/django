from django.db import models

class CourseManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) |
            models.Q(description__icontains=query)
        )

class Course(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank=True
                                   ) # blank=True diz que o campo nao é obrigatorio
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