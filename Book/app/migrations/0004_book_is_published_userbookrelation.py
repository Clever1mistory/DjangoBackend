# Generated by Django 4.2 on 2023-05-06 19:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_book_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='UserBookRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=False)),
                ('in_bookmarks', models.BooleanField(default=False)),
                ('rate', models.PositiveIntegerField(choices=[(1, 'ok'), (1, 'fine'), (1, 'good'), (1, 'amasing'), (1, 'incredible')])),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
