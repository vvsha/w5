from django.db import models

from django.db import models
from django.utils import timezone

# Create your models here.

# class — это специальное ключевое слово для определения объектов.
# Post — это имя нашей модели, мы можем поменять его при желании (специальные знаки и пробелы использовать нельзя).
# Всегда начинай имена классов с прописной буквы.

class Post(models.Model):	#  — эта строка определяет нашу модель (объект).
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)	# .ForeignKey  — ссылка на другую модель.
    title = models.CharField(max_length=200)	#  — так мы определяем текстовое поле с ограничением на количество символов.
    text = models.TextField()				#  — так определяется поле для неограниченно длинного текста.
    created_date = models.DateTimeField(		#  — дата и время.
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

	# def означает, что создаётся функция/метод, а publish — это название этого метода
	# правило для имён функций: нужно использовать строчные буквы, а пробелы заменять на подчёркивания

    def publish(self):		# метод публикации для записи
        self.published_date = timezone.now()
        self.save()

    def __str__(self):		# д.б. по 2 подчеркиваня ("dunder") с каждой стороны str
        return self.title

	# обрати внимание, что оба метода def publish(self): и def __str__(self): внутри класса имеют дополнительный отступ. 	# Поскольку в Python важны отступы, нам необходимо использовать их для методов внутри класса
	# иначе методы не будут принадлежать к классу, и при запуске программы может получиться что-то неожиданное.
