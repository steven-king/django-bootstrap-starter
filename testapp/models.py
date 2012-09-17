from django.db import models

# Create your models here.

DEFAULT_CHAR_MAX_LENGTH = 80

class Person(models.Model):
    
    name = models.CharField(max_length=DEFAULT_CHAR_MAX_LENGTH)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    
    def __unicode__(self):
        return self.name