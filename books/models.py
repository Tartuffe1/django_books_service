from django.db import models
from datetime import datetime 

class Book(models.Model):
    CATEGORY_CHOICES = (
        ('expert', 'Expert books'),
        ('classic', 'Classic literature'),
        ('antiquarian', 'Antiquarian books'),
        ('other', 'Other books'),
        ('foreign', 'Foreign books'),
    )
    
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=200)
    year = models.IntegerField(default=1)
    binding = models.CharField(max_length=10)
    pages = models.IntegerField(default=1)
    soundness = models.CharField(max_length=50)
    category = models.CharField(max_length=15, choices = CATEGORY_CHOICES)
    price = models.IntegerField(default=1)
    extra = models.CharField(max_length=200)
    date = models.DateField(default=datetime.now())
    docfile = models.FileField(upload_to='images/%Y/%m/%d')
    user_id=models.IntegerField(default=1)
    
    def __unicode__(self):
        return self.title
