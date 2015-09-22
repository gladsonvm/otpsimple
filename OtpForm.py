from django import forms

class OtpForm(forms.Form):
    token = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'otp', 'class': 'form-control'}))
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'mobile', 'class': 'form-control'}))

    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        self.request = request
        self.user_cache = None
        super(OtpForm, self).__init__(*args, **kwargs)

    def clean(self):
        fields_exists = False
        cleaned_data = super(OtpForm, self).clean()
        try:
            token = int(cleaned_data.get("token"))
            phone = int(cleaned_data.get("phone"))
            fields_exists = True
        except:
            raise ValidationError("Only Numbers are allowed for otp and mobile fields.")
        if fields_exists:
            if 0 <= token <= 99999 and 1000000000 <= phone <= 9999999999:
                print '123'
                self.user_cache = authenticate(token=token,phone=phone)
                return cleaned_data
        else:
            raise ValidationError("Enter valid credentials.")

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        self.user_cache = authenticate(token=token, phone=phone)
        return self.user_cache

    class Meta:
        model = OtpTokens
        fields = "__all__"
