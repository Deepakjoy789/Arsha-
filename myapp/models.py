from django.db import models

# Create your models here.
class Feature(models.Model):
 
    name = models.CharField(max_length =30)
    details = models.CharField(max_length = 500) 
     # Settings.py -> iNSTALLED aPPS

    
    
    """
    class Feature:
    id : int 
    name : str 
    details : str
    is_true : bool

    """