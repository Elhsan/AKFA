from .models import Order
from django.forms import ModelForm
from django import forms

genre_choices = (
    ("пластик", "пластик"),
    ("метал", "метал"),
    ("дуб", "дуб"),
    ("сосна", "сосна"),
    ("береза", "береза"),


)


class OrderForms(ModelForm):
    материал = forms.CharField(max_length=255, label="Genre", help_text="Enter main material of your order",widget=forms.Select(choices=genre_choices))
    
    class Meta:
        model = Order
        fields = ("имя","размеры","стоимость","материал",)
