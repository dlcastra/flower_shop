from django import forms

from store.models import Flower, Fertilizers, Buyer


class FlowerForm(forms.ModelForm):
    class Meta:
        model = Flower
        fields = ["name", "passport_number", "color"]


class FertilizersForm(forms.ModelForm):
    class Meta:
        model = Fertilizers
        fields = ["code", "name"]


class BuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = "__all__"
