from django.shortcuts import render, get_object_or_404, redirect
from store.forms import BuyerForm
from store.models import Flower, Order, Buyer


def get_all_flowers(request, **kwargs):
    if request.method == "GET":
        flowers = Flower.objects.all()
        return render(request, "flower_store.html", {"flowers": flowers})


def order_flower(request, flower_id):
    if request.method == "POST":
        flower = get_object_or_404(Flower, id=flower_id)
        buyer = Buyer.objects.create()
        Order.objects.create(buyer=buyer, flower=flower)
        return redirect("order_form")
    else:
        flower = get_object_or_404(Flower, id=flower_id)
        return render(request, "order_flower.html", {"flower": flower})


def order_form(request):
    if request.method == "POST":
        form = BuyerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("order_success")
    else:
        form = BuyerForm()
    return render(request, "order_form.html", {"form": form})


def order_success(request):
    return render(request, "order_success.html")
