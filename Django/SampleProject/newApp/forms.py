from django import forms
from newApp.models import User
from django.core import validators
# class Opinion_Form(forms.Form):
#     userName = forms.CharField(max_length = 10)
#     email = forms.EmailField(max_length = 100)
#     opinion = forms.CharField(widget = forms.Textarea)

class SignUp(forms.ModelForm):
    def clean(self):
        all_clean_data = super().clean()
        pwd = all_clean_data['pwd']
        vpwd = all_clean_data['vpwd']
        if(pwd!=vpwd):
            raise forms.ValidationError('Password mismatch found')
    class Meta:
        model = User
        fields = '__all__'
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','pwd')
