from django.db import models

class Center(models.Model):
    name = models.CharField(max_length=124)
    address = models.TextField()
    
    def __str__(self):
        return self.name
