# Import/Export Design Pattern

This design pattern is used when you want to export a list of objects into a CSV file and import a CSV 
file to create a list of objects.


The design pattern has several pieces that should be built as stepping stones using test-driven development.
Each step is shown by presenting code that demonstrates the pattern.


## Table App

Create a new app for table code

    $ python manage.py startapp table

config/settings.py

    INSTALLED_APPS = [  ..., 'table', ]



## Executable Django Command

Run Custom Commands

    $ python manage.py quick_test

```python
from django.core.management.base import BaseCommand, no_translations

from table.table import read_csv_file


class Command(BaseCommand):

    def handle(self, *args, **options):
        print("Quick Test")

        path = 'Documents/objects.csv'
        print(read_csv_file(path))
```


## CSV Reader
Read a file and convert into a table (list of rows)

Documents/animals.csv

```csv
1,Dog
2,Cat
3,Bird
4,Fish
```

table.py

```python
def read_csv_file(path):
    with open(path) as f:
        return [row for row in reader(f)]

class TableTest(TestCase):

    def test_read_csv(self):
        table = read_csv_file('Documents/animals.csv')
        self.assertEqual(table, [['1', 'Dog'], ['2', 'Cat'], ['3', 'Bird'], ['4', 'Fish']])
```



## CSV Writer
Write a table (list of rows) into a CSV file.   Each row is a list
of values.

```python
def export_table(model):
    records = [o.values() for o in model.objects.all()]
    write_csv_file('Documents/animals.csv', records)


class TableTest(TestCase):

    def test_write_csv(self):
        table = read_csv_file('Documents/animals.csv')
        write_csv_file('Documents/animals.csv', table)
        table = read_csv_file('Documents/animals.csv')
        self.assertEqual(table, [['1', 'Dog'], ['2', 'Cat'], ['3', 'Bird'], ['4', 'Fish']])
```


## Chapters in Book Builder

```python
class Chapter(models.Model):
    book = models.CharField(max_length=200)
    order = models.IntegerField()
    title = models.CharField(max_length=200)
```


## Create object Record

Build a Chapter object from a list of values

```python
class Chapter(models.Model):

    @staticmethod
    def import_record(values):
        c = Chapter.objects.get_or_create(book=values[0], order=values[1])[0]
        c.title = values[2]
        c.save()
        return c

row = ['Tales of Fear', 1, 'Gold Bug']
c = Chapter.import_record(row)
assert(c.title ==  'Gold Bug')
```



## Import from CSV File

For each row in table build one object

```python
for row in read_csv_file(path):
    Chapter.import_record(row)
```


## Export to CSV

For each object write one line of CSV data

```python
class Chapter(models.Model):

    def export_record(self):
        return [self.book, self.order, self.title]

chapters = Chapter.objects.filter(book=book)
table = [c.export_record(c) for c in chapters]
write_csv_file(path, table)
```



## Import/Export Test

Reading objects and them writing them should not change the CSV file

```python
class ChapterDataTest(TestCase):

    def test_chapter_import_export(self):
        book = Book.objects.get_or_create(title="The Leverage Principle", 
                                          author='Mark Seaman', 
                                          doc_path='Documents/Leverage')[0]
        first = import_chapters(book)
        export_chapters(book)
        second = import_chapters(book)
        self.assertEqual(len(Chapter.objects.all()), 15)
        self.assertEqual(second, first)
```


