from django import forms


class Cart(forms.Form):
    from_user = forms.CharField(max_length = 200)
    to_user = forms.CharField(max_length = 2000)
    image = forms.ImageField()
