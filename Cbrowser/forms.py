from django import forms
from . models import *

class enrollForm(forms.ModelForm):
    class Meta:
        model = enrollments
        fields = ['s_id','id']

class SignUp(forms.ModelForm):
    class Meta:
        model = student
        fields = ['name','s_id','age','dp','gpa']

class AddDeptForm(forms.ModelForm):
    class Meta:
        model = department
        fields = ['dept_name','d_id','d_logo']

class StudentUpdateForm(forms.Form):
    name = forms.CharField(label='Name')
    age = forms.IntegerField(label='Age')
    gpa = forms.FloatField(label='GPA')
    dp = forms.CharField(label='Link To Image')

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = course
        fields = ['name','c_id','semester','duration','dept','c_logo']

class AddAndAsignProf(forms.ModelForm):
    class Meta:
        model = prof
        fields = ['name','c_taken','p_id','dept','p_pic']
class addLinkForm(forms.ModelForm):
    class Meta:
        model = links
        fields = ['l_title','link']
