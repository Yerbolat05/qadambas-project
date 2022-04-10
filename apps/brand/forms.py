from django import forms

from brand.models import Clothes

class CreatedClothes(forms.ModelForm):

    # name = forms.CharField(
    #     max_length = 150,
    #     label = 'Имя одежды' 
    # )

    # brand = forms.CharField(
    #     max_length = 50,
    #     label = 'Брэнд'
    # )

    # img = forms.ImageField(
    #     label = 'Изображение',
    #     max_length = 255
    # )

    # country = forms.CharField(
    #     max_length = 50,
    #     label = 'Пройзводство'
    # )

    # size = forms.IntegerField(
    #     label = 'Размер'
    # )

    # type_clothes = forms.CharField(
    #     max_length = 150,
    #     label = 'Ткань'
    # )

    # categories = forms.CharField(
    #     max_length = 150,
    #     label = 'Категория'
    # )

    # price = forms.IntegerField(
    #     label = 'Стоймость'
    # )

    class Meta:
        model = Clothes
        fields = [
            'name', 'brand', 'img','country', 'size', 
            'type_clothes', 'categories', 'price'
        ]