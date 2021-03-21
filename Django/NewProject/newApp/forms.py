from django import forms
from newApp.models import User
# class Opinion_Form(forms.Form):
#     userName = forms.CharField(max_length = 10)
#     email = forms.EmailField(max_length = 100)
#     opinion = forms.CharField(widget = forms.Textarea)
class SignUp(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
