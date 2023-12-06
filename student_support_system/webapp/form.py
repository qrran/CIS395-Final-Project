from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms

from .models import Record

# add record, create new data

class CreateRecordForm(forms.ModelForm):

    class Meta:

        model = Record
        fields = ['first_name', 'last_name', 'student_id', 'student_email', 'phone_number', 'major']
    
# same logic as update, based on the same field accordingly, and from the same model which is Record (the table created in model.py)
# - Update a record

class UpdateRecordForm(forms.ModelForm):

    class Meta:

        model = Record
        fields = ['first_name', 'last_name', 'student_id', 'student_email', 'phone_number', 'major']


    