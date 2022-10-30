from django import forms
from farms.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            'fname':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Juan Dela Cruz'}),
            'email_address':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'juandelacruz@gmail.com'}),
            'subject':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the message'}),
            'message':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Body of the message'}),
        }