from django import forms

class RoomForm(forms.Form):
    room = forms.CharField(label='Room', max_length=100)
    password = forms.CharField(label='Password', max_length=30, widget=forms.PasswordInput)

