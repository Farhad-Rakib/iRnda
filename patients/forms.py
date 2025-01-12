# forms.py
from django import forms
from .models import Patient, PatientDetail

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'date_of_birth', 'birth_weight', 'sex']
    
    # Apply Bootstrap classes to form fields
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Patient Name'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Age'}))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD', 'type': 'date'}))
    birth_weight = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Birth Weight'}))
    sex = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=[('M', 'Male'), ('F', 'Female')])

class PatientDetailForm(forms.ModelForm):
    class Meta:
        model = PatientDetail
        fields = ['mother_name', 'father_name', 'mother_education', 'father_education', 
                  'living_area', 'father_profession', 'mother_profession', 'father_monthly_income']
    
    # Apply Bootstrap classes to form fields
    mother_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Mother\'s Name'}))
    father_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Father\'s Name'}))
    mother_education = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Mother\'s Education'}))
    father_education = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Father\'s Education'}))
    living_area = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Living Area'}))
    father_profession = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Father\'s Profession'}))
    mother_profession = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Mother\'s Profession'}))
    father_monthly_income = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Father\'s Monthly Income'}))
    #number_of_siblings = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Number of Siblings'}))

