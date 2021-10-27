from django.db import models
from django.urls.base import reverse_lazy


# --------------------
# Book
#
# title - title of the book
# author - name of author
# description - summary of the book

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField(default='None')
    doc_path = models.CharField(max_length=200, default='Documents/Leverage')

    def __str__(self):
        return f'{self.pk} - {self.title} by {self.author}'

    def get_absolute_url(self):
        return reverse_lazy('book_detail', args=[str(self.id)])


# --------------------
# Chapter
#
# book - points to book object
# order - chapter order
# title - title text of chapter
# markdown - markdown text
# document - path to markdown file

class Chapter(models.Model):
    book = models.CharField(max_length=200, default="Leverage Principle")
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
