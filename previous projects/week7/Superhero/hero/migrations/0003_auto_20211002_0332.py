# Generated by Django 3.2.6 on 2021-10-02 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0002_auto_20211002_0304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='strength',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='hero',
            name='weakness',
            field=models.TextField(),
        ),
    ]
