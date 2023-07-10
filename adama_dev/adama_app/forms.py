from django import forms
from .models import User_Data


class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = User_Data
        fields = ['Name', 'Username', 'Password', 'User_Role', 'Shift', 'Status', 'plant_name', 'line_name']