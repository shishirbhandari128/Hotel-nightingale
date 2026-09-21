from django import forms
from django.core.exceptions import ValidationError

INQUIRY_TYPE_CHOICES = [
    ('general', 'General Inquiry'),
    ('reservation', 'Room Reservation'),
    ('events', 'Events'),
    ('concierge', 'Concierge'),
]


class ContactForm(forms.Form):
    full_name = forms.CharField(
        max_length=120,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Your full name',
        }),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'you@example.com',
        }),
    )
    phone = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': '+1 (555) 000-0000',
        }),
    )
    inquiry_type = forms.ChoiceField(
        choices=INQUIRY_TYPE_CHOICES,
        required=True,
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    check_in = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
    )
    check_out = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
    )
    guests = forms.IntegerField(
        required=False,
        min_value=1,
        max_value=10,
        initial=2,
        widget=forms.NumberInput(attrs={'class': 'form-input', 'min': 1, 'max': 10}),
    )
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-textarea',
            'rows': 5,
            'placeholder': 'Tell us how we can assist you...',
        }),
    )
    honeypot = forms.CharField(
        required=False,
        widget=forms.HiddenInput(),
    )

    def clean_honeypot(self):
        value = self.cleaned_data.get('honeypot')
        if value:
            raise ValidationError('Bot submission detected.')
        return value
