from django import forms

class RasPiForm(forms.Form):
    mac_address = forms.CharField(
        label = "MACアドレス",
        max_length = 17,
        widget = forms.TextInput(attrs={'placeholder':'01:00:5e:90:10:d5'}),
    )
    in_use = forms.BooleanField(
        label = "有効／無効",
        initial = 1
    )
