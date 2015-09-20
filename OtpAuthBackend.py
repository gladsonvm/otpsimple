from django.contrib.auth.models import User
from core.models import OtpTokens, UserProfile
import datetime
from django.utils import timezone
import json

class OtpAuthBackend(object):
    def authenticate(self, token=None, phone=None):
        try:
            token = OtpTokens.objects.get(otp=token, phone=phone)
        except:
            return json.dumps({'Error': 'TokenDoesnotExists'})
        if token.user.is_active and (datetime.datetime.now(timezone.utc)-token.created_at).seconds<300:
            try:
                profile = UserProfile.objects.get(user=token.user)
            except:
                return json.dumps({'Error': 'UserProfileDoesNotExists'})
            if profile.mobile_no == phone:
                return token.user
            else:
                return json.dumps({'Error': 'PhoneDoesNotExists'})
        else:
            return json.dumps({'Error': 'TokenExpired'})

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
