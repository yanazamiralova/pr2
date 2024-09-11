from django.db import models


class Ad(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='ads', on_delete=models.CASCADE)
    price = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ['created']


class Review(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    owner = models.ForeignKey('auth.User', related_name='reviews', on_delete=models.CASCADE)
    ad = models.ForeignKey('Ad', related_name='reviews', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    owner = models.ForeignKey('auth.User', related_name='categories', on_delete=models.CASCADE)
    ads = models.ManyToManyField('Ad', related_name='categories', blank=True)

    class Meta:
        verbose_name_plural = 'categories'