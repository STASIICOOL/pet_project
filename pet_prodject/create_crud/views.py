from django.shortcuts import render
from create_crud.forms import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
# Create your views here.

def create_view_housing(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = HousingForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "create_view_housing.html", context)


def list_view_housing(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = HousingForm.objects.all()

    return render(request, "list_view_housing.html", context)


def update_view_housing(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(HousingForm, id=id)

    # pass the object as instance in form
    form = HousingForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

def detail_view_housing(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = HousingForm.objects.get(id=id)

    return render(request, "detail_view_housing.html", context)


    # add form dictionary to context
    context["form"] = form

    return render(request, "update_view_housing.html", context)



def create_view_number_housing(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = Number_housingForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "create_view_number_housing.html", context)


def list_view_number_housing(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = Number_housingForm.objects.all()

    return render(request, "list_view_number_housing.html", context)


def update_view_number_housing(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Number_housingForm, id=id)

    # pass the object as instance in form
    form = Number_housingForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

def detail_view_number_housing(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = Number_housingForm.objects.get(id=id)

    return render(request, "detail_view_number_housing.html", context)


    # add form dictionary to context
    context["form"] = form

    return render(request, "update_view_number_housing.html", context)



def create_view_city(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = CityForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "create_view_city.html", context)


def list_view_city(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = CityForm.objects.all()

    return render(request, "list_view_city.html", context)


def update_view_city(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(CityForm, id=id)

    # pass the object as instance in form
    form = CityForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

def detail_view_city(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = CityForm.objects.get(id=id)

    return render(request, "detail_view_city.html", context)


    # add form dictionary to context
    context["form"] = form

    return render(request, "update_view_city.html", context)



def create_view_category(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "create_view_category.html", context)


def list_view_category(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = CategoryForm.objects.all()

    return render(request, "list_view_category.html", context)


def update_view_category(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(CategoryForm, id=id)

    # pass the object as instance in form
    form = CategoryForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

def detail_view_category(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = CategoryForm.objects.get(id=id)

    return render(request, "detail_view_category.html", context)


    # add form dictionary to context
    context["form"] = form

    return render(request, "update_view_category.html", context)



def create_view_post(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "create_view_post.html", context)


def list_view_post(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = PostForm.objects.all()

    return render(request, "list_view_post.html", context)


def update_view_post(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(PostForm, id=id)

    # pass the object as instance in form
    form = PostForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

def detail_view_post(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = PostForm.objects.get(id=id)

    return render(request, "detail_view_post.html", context)


    # add form dictionary to context
    context["form"] = form

    return render(request, "update_view_post.html", context)



def create_view_delivery(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = DeliveryForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "create_view_delivery.html", context)


def list_view_delivery(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = DeliveryForm.objects.all()

    return render(request, "list_view_delivery.html", context)


def update_view_delivery(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(DeliveryForm, id=id)

    # pass the object as instance in form
    form = DeliveryForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

def detail_view_delivery(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = DeliveryForm.objects.get(id=id)

    return render(request, "detail_view_delivery.html", context)


    # add form dictionary to context
    context["form"] = form

    return render(request, "update_view_delivery.html", context)



def create_view_food(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = FoodForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "create_view_food.html", context)


def list_view_food(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = FoodForm.objects.all()

    return render(request, "list_view_food.html", context)


def update_view_food(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(FoodForm, id=id)

    # pass the object as instance in form
    form = FoodForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

def detail_view_food(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = FoodForm.objects.get(id=id)

    return render(request, "detail_view_food.html", context)


    # add form dictionary to context
    context["form"] = form

    return render(request, "update_view_food.html", context)



def create_view_food_place(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = FoodPlaceForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "create_view_food_place.html", context)


def list_view_food_place(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = FoodPlaceForm.objects.all()

    return render(request, "list_view_food_place.html", context)


def update_view_food_place(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(FoodPlaceForm, id=id)

    # pass the object as instance in form
    form = FoodPlaceForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

def detail_view_food_place(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = FoodPlaceForm.objects.get(id=id)

    return render(request, "detail_view_food_place.html", context)


    # add form dictionary to context
    context["form"] = form

    return render(request, "update_view_food_place.html", context)



def create_view_layout(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = LayoutForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "create_view_layout.html", context)


def list_view_layout(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = LayoutForm.objects.all()

    return render(request, "list_view_layout.html", context)


def update_view_layout(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(LayoutForm, id=id)

    # pass the object as instance in form
    form = LayoutForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

def detail_view_layout(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = LayoutForm.objects.get(id=id)

    return render(request, "detail_view_layout.html", context)


    # add form dictionary to context
    context["form"] = form

    return render(request, "update_view_layout.html", context)



def create_view_news(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = NewsForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "create_view_news.html", context)


def list_view_news(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = NewsForm.objects.all()

    return render(request, "list_view_news.html", context)


def update_view_news(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(NewsForm, id=id)

    # pass the object as instance in form
    form = NewsForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

def detail_view_news(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = NewsForm.objects.get(id=id)

    return render(request, "detail_view_news.html", context)


    # add form dictionary to context
    context["form"] = form

    return render(request, "update_view_news.html", context)



def create_view_interesting_place(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = InterestingPlaceForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "create_view_interesting_place.html", context)


def list_view_interesting_place(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = InterestingPlaceForm.objects.all()

    return render(request, "list_view_interesting_place.html", context)


def update_view_interesting_place(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(InterestingPlaceForm, id=id)

    # pass the object as instance in form
    form = InterestingPlaceForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

def detail_view_interesting_place(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = InterestingPlaceForm.objects.get(id=id)

    return render(request, "detail_view_interesting_place.html", context)


    # add form dictionary to context
    context["form"] = form

    return render(request, "update_view_interesting_place.html", context)


