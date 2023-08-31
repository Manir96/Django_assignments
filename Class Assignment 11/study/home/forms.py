from django import forms


class userRegistration(forms.Form):
    First_Name = forms.CharField()
    Last_Name = forms.CharField(disabled=True)
    Email = forms.EmailField(label='Email_Address')
    batch = forms.IntegerField(label_suffix='==', initial='03')
    Phone = forms.IntegerField(widget=forms.HiddenInput())
    texarea = forms.CharField(widget=forms.Textarea())
    password = forms.CharField(widget=forms.PasswordInput())
    checkbox = forms.CharField(widget=forms.CheckboxInput())
    file = forms.CharField(widget=forms.FileInput())