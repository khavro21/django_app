from django.forms import ModelForm

from blog.models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'