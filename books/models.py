from django.db import models

# Create your models here.
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
    category = models.CharField(max_length=15, choices = CATEGORY_CHOICES)
    price= models.IntegerField()
    docfile = models.FileField(upload_to='images/%Y/%m/%d', default='images/default.jpg')
    
    def __unicode__(self):
        return self.title
