from django.db import models

class Author(models.Model):
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    middle_name = models.CharField('Отчество', max_length=50, blank=True)

    email = models.EmailField('Email', blank=True)
    phone = models.PositiveIntegerField('Телефон', null=True, blank=True)

    def __str__(self):
        return ' '.join((self.last_name, self.first_name, self.middle_name))

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Tag(models.Model):
    name = models.CharField('Название', max_length=50)
    is_active = models.BooleanField('Флаг активности', default=False)

    def __str__(self):
        return '{} {}'.format('🞎' if self.is_active else '☑', self.name)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Book(models.Model):
    name = models.CharField('Название', max_length=100)
    description = models.CharField('Краткое описание', max_length=500)
    preview = models.ImageField('Изображение-превью', upload_to='books/previews/', null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    tags = models.ManyToManyField(Tag, verbose_name='Теги')

    pub_at = models.DateField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return '{}: {}'.format(self.author, self.name)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
