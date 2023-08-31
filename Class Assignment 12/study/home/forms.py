from django.core.validators import RegexValidator
from django import forms


class userRegistration(forms.Form):
    First_Name = forms.CharField()
    Last_Name = forms.CharField(required=False, help_text = 'must fill the field')
    Email = forms.EmailField(label='Email_Address')
    batch = forms.IntegerField(label_suffix='==', initial='03')
    # Phone = forms.IntegerField()
    # mobile_number = forms.CharField(label='Phone Number',  validators=[validator.RegexValidator(r'^\d{11}$', message='Enter your 11-digit phone number')])
    phone_regex = RegexValidator(regex=r'^\+?88?\d{9,11}$',message="Phone number must be entered in the format: '+88'. Up to 11 digits allowed.")
    phone = forms.CharField(validators=[phone_regex],required=True,label="Phone")
    texarea = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':20}))
    password = forms.CharField(widget=forms.PasswordInput(),min_length=6,max_length=15)
    re_password = forms.CharField(widget=forms.PasswordInput(),min_length=6,max_length=15)
    checkbox = forms.CharField(widget=forms.CheckboxInput())
    # file = forms.CharField(widget=forms.FileInput())
    payment = forms.DecimalField(min_value=2000, max_value=5000)
    django = forms.BooleanField()
    
    
    def clean(self):
        cleaned_data = super().clean()
        password_match = self.cleaned_data['password']
        re_password_match = self.cleaned_data['re_password']
        if password_match != re_password_match:
            raise forms.ValidationError('password doesnot match')