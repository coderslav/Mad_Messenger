from allauth.account.forms import SignupForm
from django import forms

SEX_CHOICES = (('M', 'Мужчина'), ('W', 'Женщина'), ('N', 'Неопределенный'))


class CustomSignUpForm(SignupForm):
    age = forms.IntegerField(label='id_age', required=True,
                             widget=forms.TextInput(
                                 attrs={"type": "number", "placeholder": "Возраст", "min": "1"}
                             ))
    sex = forms.CharField(label='id_sex', required=True, widget=forms.Select(choices=SEX_CHOICES))
