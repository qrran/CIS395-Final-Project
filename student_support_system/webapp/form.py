from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms

from .models import Record, CommunityEngagement

# add record, create new data

class CreateRecordForm(forms.ModelForm):

    class Meta:

        model = Record
        fields = ['first_name', 'last_name', 'student_id', 'student_email', 'phone_number', 'major', 'gpa']

class CreateCommunityEngagementForm(forms.ModelForm):

    class Meta:

        model = CommunityEngagement
        fields = ['participation', 'organization_name', 'activity_name','role']
    
# same logic as update, based on the same field accordingly, and from the same model which is Record (the table created in model.py)
# - Update a record

class UpdateRecordForm(forms.ModelForm):
    class Meta:

        model = Record
        fields = ['first_name', 'last_name', 'student_id', 'student_email', 'phone_number', 'major', 'gpa']

class UpdateCommunityEngagementForm(forms.ModelForm):
    student = forms.ModelChoiceField(queryset=Record.objects.all(), empty_label="Select a student")
    class Meta:

        model = CommunityEngagement
        fields = ['participation', 'organization_name', 'activity_name','role']
    

    