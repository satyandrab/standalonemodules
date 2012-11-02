from django.db import models
from datetime import datetime  

class BetaRegistration(models.Model):
    """
    """
    email = models.EmailField(unique=True)
    url_hash = models.CharField(max_length=32, unique=True)
    invite_hash = models.CharField(max_length=32, unique=True)
    time_stamp = models.DateTimeField(default=datetime.now, blank=True)
    click_pnts = models.IntegerField(default=0)
    click_ips = models.ManyToManyField('IPLog', null=True)
    signup_pnts = models.IntegerField(default=0)
    #refered_by relation is to other beta registration objects.
    #When individuals register in the future (process through django-registration) that is when we will create a 'user'
    refered_by = models.ForeignKey('self', null = True)  
    email_verified = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.email


class IPLog(models.Model):
    ip = models.IPAddressField(unique=True)

    def __unicode__(self):
        return self.ip