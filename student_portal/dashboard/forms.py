from django import forms
from django.core.exceptions import ValidationError
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'ant-input', 'placeholder': 'Enter student name', 'style': 'padding: 8px 12px; border-radius: 6px;'}),
            'email': forms.EmailInput(attrs={'class': 'ant-input', 'placeholder': 'Enter email address', 'style': 'padding: 8px 12px; border-radius: 6px;'}),
            'course': forms.TextInput(attrs={'class': 'ant-input', 'placeholder': 'Enter course name', 'style': 'padding: 8px 12px; border-radius: 6px;'}),
            'marks': forms.NumberInput(attrs={'class': 'ant-input', 'placeholder': 'Enter marks (0-100)', 'style': 'padding: 8px 12px; border-radius: 6px;'}),
        }

    def clean_marks(self):
        marks = self.cleaned_data.get('marks')
        if marks is not None and (marks < 0 or marks > 100):
            raise ValidationError("Marks must be between 0 and 100.")
        return marks
