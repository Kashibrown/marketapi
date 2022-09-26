from django.db import models

# Create your models here.
class Market(models.Model):
    section= (
        ('cow_meat', 'Cow Meat'),
        ('fish', 'Fish'),
        ('turkey', 'Turkey'),
        ('chicken', 'Chicken'),
    )
    name = models.CharField(max_length=100)
    options = models.CharField('options:',max_length=20, choices=section)
    buying = models.BooleanField(default=False, blank=True, null=True) 
    
    def __str__(self):
        return self.name
    