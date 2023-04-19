from django.db import models
import os
import datetime
# Create your models here.

class Alzhimer(models.Model):

    def filepath(request, filename):
        old_filename = filename
        timenow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
        filename = "%s%s" % (timenow, old_filename)
        return os.path.join("uploads", filename)
    
    name = models.CharField(max_length=15)
    image = models.ImageField(upload_to =filepath , null=True, blank=True)

    def __str__(self):
    	return  self.name