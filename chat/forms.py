from allauth.account.forms import SignupForm
from django import forms


class CustomSignUpForm(SignupForm):
    age = forms.IntegerField(label='id_age', required=True,
                             widget=forms.TextInput(
                                 attrs={"type": "number", "placeholder": "Возраст", "min": "1"}
                             ))

    def save(self, request):
        user = super(CustomSignUpForm, self).save(request)
        user.age = int(self.cleaned_data['age'])
        user.save()
        return user
