from django import forms
from .models import Record

#Create Add Record form

class AddRecordForm(forms.ModelForm):
  first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "First Name", "class":"form-control"}), label="")
  last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Last Name", "class":"form-control"}), label="")
  phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Phone no", "class":"form-control"}), label="")
  city =  forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "City Name", "class":"form-control"}), label="")


  class Meta:
    model = Record
    fields = ['first_name', 'last_name', 'phone', 'city']