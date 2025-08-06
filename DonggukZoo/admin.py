# DonggukZoo/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms
from .models import CustomUser

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('student_id', 'username', 'usertype')
        widgets = {
            'student_id': forms.TextInput(attrs={'style': 'width: 250px;'}),
        }

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserCreationForm
    
    list_display = ('student_id', 'username', 'usertype', 'is_staff')
    list_filter = ('usertype', 'is_staff', 'is_active')
    search_fields = ('student_id', 'username')
    ordering = ('student_id',)

    fieldsets = (
        (None, {'fields': ('student_id', 'password')}),
        ('Personal info', {'fields': ('username', 'usertype')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {'fields': ('student_id', 'password', 'username', 'usertype')}),
    )