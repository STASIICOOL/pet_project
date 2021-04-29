from django import forms
from booking.models import Housing, Number_housing
from city.models import City
from custom_category.models import Category, Post
from delivery.models import Delivery
from food_point.models import Food, FoodPlace
from interest_place.models import InterestingPlace
from layout.models import Layout
from news.models import News


# creating a form
class HousingForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Housing

        # specify fields to be used
        exclude = ['image']


class Number_housingForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Number_housing

        # specify fields to be used
        exclude = ['image']


class CityForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = City

        # specify fields to be used
        exclude = ['flag', 'emblem']


class CategoryForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Category

        # specify fields to be used
        fields = "__all__"


class PostForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Post

        # specify fields to be used
        exclude = ['image']


class DeliveryForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Delivery

        # specify fields to be used
        fields = "__all__"


class FoodForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Food

        # specify fields to be used
        exclude = ['image']


class FoodPlaceForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = FoodPlace

        # specify fields to be used
        fields = "__all__"


class LayoutForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Layout

        # specify fields to be used
        fields = "__all__"


class NewsForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = News

        # specify fields to be used
        exclude = ['image']


class InterestingPlaceForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = InterestingPlace

        # specify fields to be used
        exclude = ['image']