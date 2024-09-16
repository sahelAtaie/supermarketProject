from django.db import models

# Create your models here.
from django.db import models


class Product(models.Model):
    code = None
    name = None
    price = None
    inventory = None

    def increase_inventory(self, amount):
        pass

    def decrease_inventory(self, amount):
        pass


class Customer(models.Model):
    user = None
    phone = None
    address = None
    balance = None

    def deposit(self, amount):
        pass

    def spend(self, amount):
        pass


class OrderRow(models.Model):
    product = None
    order = None
    amount = None


class Order(models.Model):
    customer = None
    order_time = None
    total_price = None
    status = None

    @staticmethod
    def initiate(customer):
        pass

    def add_product(self, product, amount):
        pass

    def remove_product(self, product, amount=None):
        pass

    def submit(self):
        pass

    def cancel(self):
        pass

    def send(self):
        pass
