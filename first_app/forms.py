from django import forms
from django.core import validators
from first_app import models

# class user_form(forms.Form):
#     # user_name = forms.CharField( required=True, label="Full Name", widget= forms.TextInput(attrs ={'placeholder': 'Enter Your Name'}))
#     # user_email = forms.EmailField(label="User Email", widget = forms.TextInput(attrs={'placeholder': 'Enter Your Email'}))

#     # user_dob = forms.DateField(label="User DOB", widget= forms.TextInput(attrs={'type':'date'}))
#     # boolean_field = forms.BooleanField(required=False)

#     # field = forms.CharField(max_length= 15, min_length=5)
#     # field = forms.ChoiceField(choices=(('', 'Select Option'),(1, "Worst"),
#     #     (2, "Bad"),
#     #     (3, "Not Bad"),
#     #     (4, "Good"),
#     #     (5, "Excellent!")))

#     name = forms.CharField(validators=[validators.MaxLengthValidator(10), validators.MinLengthValidator(5)])

# class MusicianForm(forms.ModelForm):
#     class Meta: 
#         model = models.Musician
#         fields = "__all__"

class MusicianForm(forms.ModelForm):
    class Meta:
        model = models.Musician
        fields = '__all__'

class AlbumForm(forms.ModelForm):
    release_date = forms.DateField(widget= forms.TextInput(attrs= {'type': 'date'}))
    class Meta:
        model = models.Album
        fields = '__all__'

