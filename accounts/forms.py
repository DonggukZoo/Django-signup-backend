from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    student_id = forms.CharField(required=True, label='학번')

    class Meta:
        model = User
        fields = ['student_id', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['student_id']  # 학번을 username에 저장
        if commit:
            user.save()
        return user