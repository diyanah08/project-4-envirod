from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=225, blank=False)
    image = models.ImageField(blank=True, null=True)
    sku = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    cost = models.IntegerField(blank=False)
    quantity = models.IntegerField(blank=False, default=0)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    
    def __str__(self):
        return self.sku + " : " + self.name + " [ " + str(self.date) + " , " + str(self.start_time) + " ] "
        
    def getCostInDollars(self):
        return self.cost/100
        
class Location(models.Model):
    name= models.CharField(max_length=255, blank=False)
    
    def __str__(self):
        return self.name
        
class Tag(models.Model):
    name = models.CharField(max_length=100, blank=False)
    
    def __str__(self):
        return self.name
        
class CreateEvent(models.Model):
    name = models.CharField(max_length=225, blank=False)
    phone_number = models.CharField(max_length=225, blank=False)
    event_title = models.CharField(max_length=225, blank=False)
    description = models.TextField(blank=False)
    cost = models.IntegerField(blank=False)
    seats = models.IntegerField(blank=False, default=0)
    date = models.DateField()
    start_time = models.TimeField()
    hours_needed = models.IntegerField(blank=False)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    
    def __str__(self):
        return self.name + " : " + self.phone_number + " [ " + self.event_title + " - " + str(self.date) + " , " + str(self.start_time) + " ] "
        
    def getCostInDollars(self):
        return self.cost * 100