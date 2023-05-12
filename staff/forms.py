from django import forms

class EmployeeLoginForm(forms.Form):
    employee_id = forms.CharField(label='Employee ID', max_length=255)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
