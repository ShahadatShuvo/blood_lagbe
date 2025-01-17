from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
User = get_user_model()


class LoginForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('phone', 'password')

    def clean(self):
        if self.is_valid():
            phone = self.cleaned_data['phone']
            password = self.cleaned_data['password']
            if not authenticate(phone=phone, password=password):
                raise forms.ValidationError("Invalid login")


class RegistrationForm(UserCreationForm):
    class Meta:
        """Meta class"""
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone')

        def clean_phone(self, *args, **kwargs):
            phone = self.cleaned_data.get('phone')
            print("\n -------------" + phone[0:2])
            if phone[:2] == '01':
                if phone[:3] == '010' or phone[:3] == '011' or phone[:3] == '012':
                    raise forms.ValidationError('Invalid Phone number')
                else:
                    return phone
            else:
                raise forms.ValidationError('Invalid Phone number')
