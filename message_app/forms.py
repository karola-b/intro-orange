from django import forms

from message_app.models import Message


class MessageForm(forms.Form):
    CHOICES = (
        ('question', 'pytanie'),
        ('other', 'inne'),
    )
    email = forms.EmailField()
    category = forms.ChoiceField(choices=CHOICES, label="Kategoria")
    subject = forms.CharField(label="Tytuł")
    body = forms.CharField(label="Treść", widget=forms.Textarea)
    fav_date = forms.DateField(
        label="Ulubiona data", widget=forms.NumberInput(attrs={'type': 'date'}))
    fav_time = forms.TimeField(
        label="Ulubiona godzina", widget=forms.NumberInput(attrs={'type': 'time'}))


class MessageModelForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

        labels = {
            'email': "Email",
            'category': "Kategoria",
            'subject': "Tytuł",
            'body': "Treść",
            'fav_date': "Ulubiona data",
            'fav_time': "Ulubiona godzina",

        }

        widgets = {
            'body': forms.Textarea(),
            'fav_date': forms.NumberInput(attrs={'type': 'date'}),
            'fav_time': forms.NumberInput(attrs={'type': 'time'}),
        }
