from django import forms


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
