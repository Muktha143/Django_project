from django import forms
from .models import UserData

class UserForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['full_name', 'dob', 'father_name', 'mobile_number', 'address', 'gender', 'state', 'pincode', 'image']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter full name'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter father's name"}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter 10-digit mobile number', 'pattern': '\\d{10}', 'maxlength': '10'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter address'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'state': forms.Select(attrs={'class': 'form-select'}),
            'pincode': forms.Select(attrs={'class': 'form-select'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
    
    def clean_mobile_number(self):
        mobile = self.cleaned_data.get('mobile_number')
        if mobile and (not mobile.isdigit() or len(mobile) != 10):
            raise forms.ValidationError("Mobile number must be exactly 10 digits.")
        return mobile

class AadhaarSearchForm(forms.Form):
    aadhaar_number = forms.CharField(
        max_length=12,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Aadhaar number'})
    )
    pan_number = forms.CharField(
        max_length=10,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter PAN number'})
    )