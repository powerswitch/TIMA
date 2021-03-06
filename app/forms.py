import autocomplete_light
from django import forms
from django.contrib.auth.forms import UserChangeForm as AuthUserChangeForm, UserCreationForm as AuthUserCreationForm
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext as _

class UserChangeForm(AuthUserChangeForm):
    cultural_background = forms.CharField(label=_('Cultural background'), required=False, widget=forms.TextInput(attrs={'autocomplete':'off', 'class':'form-control'}))

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'autocomplete':'off', 'class':'form-control'})
        self.fields['email'].widget = forms.EmailInput(attrs={'autocomplete':'off', 'class':'form-control'})
        self.fields['first_name'].widget = forms.TextInput(attrs={'autocomplete':'off', 'class':'form-control'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'autocomplete':'off', 'class':'form-control'})
        if 'cultural_background' in kwargs:
            self.fields['cultural_background'].value = kwargs['cultural_background']

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

class UserCreationForm(AuthUserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'autocomplete':'off', 'class':'form-control'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'autocomplete':'off', 'class':'form-control'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'autocomplete':'off', 'class':'form-control'})

class NewsletterForm(forms.Form):
    words = autocomplete_light.ModelMultipleChoiceField('WordAutocomplete', label=_('Words'))
