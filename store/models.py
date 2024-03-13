from django.db import models


class Fertilizers(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=150)


class Flower(models.Model):
    name = models.CharField(max_length=100)
    passport_number = models.CharField(max_length=150)
    color = models.CharField(max_length=50)
    fertilizer = models.ForeignKey(Fertilizers, on_delete=models.CASCADE, related_name="fertilizer")
    price = models.IntegerField(null=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)


class Buyer(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, null=True)
    email = models.EmailField()
    address = models.CharField(max_length=150)


class Order(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name="buyer")
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE, related_name="flower")
