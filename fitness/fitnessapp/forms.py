from django import forms
from .models import Goal ,Workout,UserDetails

class  UserDetailsForm(forms.ModelForm):
    class Meta:
        model =  UserDetails
        fields=['username','email']

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['newactivity']


class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['activity', 'target']
        labels = {
            'activity': 'Activity',
            'target': 'Target (in km)'
        }
