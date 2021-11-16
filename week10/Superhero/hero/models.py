from django.db import models
from django.urls.base import reverse_lazy


class Hero (models.Model):
    name = models.CharField(max_length=100)
    identity = models.CharField(max_length=100, default="none")
    description = models.TextField()
    image = models.CharField(max_length=200)
    strength = models.TextField()
    weakness = models.TextField()

    def __str__(self):
        return f'{self.name} - Description: {self.description}'

    def get_absolute_url(self):
        return reverse_lazy('hero_list')


class Chapter(models.Model):
    book = models.CharField(max_length=200, default="Default")
    # book = models.ForeignKey(Book, on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=200)
    markdown = models.TextField()
    html = models.TextField()
    document = models.CharField(max_length=200)

    def export_record(self):
        return [self.book, self.order, self.title]

    @staticmethod
    def import_record(values):
        c = Chapter.objects.get_or_create(book=values[0], order=values[1])[0]
        c.title = values[2]
        c.save()

    def __str__(self):
        return f'{self.book.title} - {self.order} - {self.title}'
