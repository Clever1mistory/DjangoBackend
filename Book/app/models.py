from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    author_name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL,
                              null=True, related_name='my_books')
    is_published = models.BooleanField(default=True)
    readers = models.ManyToManyField(User, through='UserBookRelation', related_name='books')
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name


class UserBookRelation(models.Model):
    RATE_CHOICES = (
        (1, 'ok'),
        (2, 'fine'),
        (3, 'good'),
        (4, 'amasing'),
        (5, 'incredible'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    in_bookmarks = models.BooleanField(default=False)
    rate = models.PositiveIntegerField(choices=RATE_CHOICES, null=True)

    def __str__(self):
        return f' {self.user.username}:  {self.book.name}, Rate: {self.rate}'

    def __init__(self, *args, **kwargs):
        super(UserBookRelation, self).__init__(*args, **kwargs)
        self.old_rate = self.rate

    def save(self, *args, **kwargs):
        creating = not self.pk

        super().save(*args, **kwargs)

        if self.old_rate != self.rate or creating:
            from app.logic import set_rating
            set_rating(self.book)