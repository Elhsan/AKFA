from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Orders


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True,
                             help_text="We never share your email with anyone else.")

    class Meta:
        model = User
        fields = ('username', 'email',
                  'password1', 'password2')









genre_choices = (
    ("пластик", "пластик"),
    ("метал", "метал"),

)
instance = None

class OrderForm(forms.ModelForm):
    material = forms.CharField(max_length=255, label="Genre", help_text="Enter main material of your order",
                            widget=forms.Select(choices=genre_choices))
    class Meta:
        model = Orders
        fields = ['name', 'sizes', 'material', 'price']

    def save(self, commit=True):
        if commit:
            self.instance.save()
        else:
            return self.instance
