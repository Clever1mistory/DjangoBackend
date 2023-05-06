# Generated by Django 4.2 on 2023-05-06 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_book_readers_alter_book_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbookrelation',
            name='rate',
            field=models.PositiveIntegerField(choices=[(1, 'ok'), (2, 'fine'), (3, 'good'), (4, 'amasing'), (5, 'incredible')]),
        ),
    ]
