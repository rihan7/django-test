
from django import forms
from .models import CustomUserModel


class register_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Type your password'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Type your password'
    }))

    class Meta:
        model = CustomUserModel
        fields = ['first_name', 'last_name', 'email', 'phone']

    def __init__(self, *args, **kwargs):
        super(register_form, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        clean_data = super().clean()
        password = clean_data.get('password')
        c_password = clean_data.get('confirm_password')

        if password != c_password:
            raise forms.ValidationError(
                'Confirm password not same'
            )
