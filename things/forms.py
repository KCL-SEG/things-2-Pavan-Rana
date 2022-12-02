"""Forms of the project."""

# Create your forms here.
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class ThingForm(forms.Form):
    name = forms.CharField(label='name', max_length=35)
    description = forms.CharField(label='description',widget=forms.Textarea(), max_length=120)
    quantity = forms.IntegerField(label='quantity',widget=forms.NumberInput(),validators=[
            MaxValueValidator(50),
            MinValueValidator(0)
        ])
