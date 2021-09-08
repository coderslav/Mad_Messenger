from allauth.account.forms import SignupForm
from django import forms


class CustomSignUpForm(SignupForm):
    age = forms.IntegerField(label='id_age', required=True,
                             widget=forms.TextInput(
                                 attrs={"type": "number", "placeholder": "Возраст", "min": "1"}
                             ))
