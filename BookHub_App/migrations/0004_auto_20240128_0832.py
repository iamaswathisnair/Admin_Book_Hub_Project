# Generated by Django 3.2.5 on 2024-01-28 03:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookHub_App', '0003_books_sr'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books_sr',
            old_name='book_id',
            new_name='book',
        ),
        migrations.RenameField(
            model_name='books_sr',
            old_name='book_name',
            new_name='name',
        ),
    ]
