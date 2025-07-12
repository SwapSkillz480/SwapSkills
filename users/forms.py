from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['location', 'profile_photo', 'skills_offered', 'skills_wanted', 'availability', 'is_public'] 