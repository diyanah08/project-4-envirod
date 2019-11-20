from django.db import models

# Create your models here.
class CartItem(models.Model):
    
    events = models.ForeignKey('events.Event', on_delete=models.CASCADE)
    owner = models.ForeignKey('accounts.MyUser', on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False, default=0)
    
    def __str__(self):
        return self.events.name + " x " + str(self.quantity)