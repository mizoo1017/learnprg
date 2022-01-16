from django import forms
from .models import Item

class PutupForm(forms.ModelForm):
  class Meta:
    model = Item
    fields = ('title', 'description', 'image', 'start_price', 'condition')