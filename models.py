from django.db import models
from django.contrib.auth.models import User

class OtpTokens(models.Model):
    otp = models.IntegerField(null=True, blank=True)
    phone = models.CharField(null=True, blank=True, max_length=15)
    user = models.ForeignKey(User, null=True, blank=True)
    is_valid = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return unicode(self.otp)
