
from django import forms
from .models import Patient
from rwutils.phone import format_phone


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'date_of_birth',
            'gender',
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Enter first name',
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Enter last name',
            }),
            'phone_number': forms.TextInput(attrs={
                'placeholder': 'e.g. 0788123456',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter email (optional)',
            }),
            'date_of_birth': forms.DateInput(attrs={
                'type': 'date',
            }),
        }

    def clean_phone_number(self):
        phone = self.cleaned_data['phone_number']

        try:
            return format_phone(phone)
        except ValueError:
            raise forms.ValidationError(
                'Enter a valid Rwandan phone number, '
                'e.g. 0788123456 or +250788123456.'
            )
