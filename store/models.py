from django.db import models


# Create your models here.
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Collection(models.Model):
    title = models.CharField(max_length=100)
    featured_product = models.ForeignKey(
        'Product',
        on_delete=models.SET_NULL,
        null=True,
        related_name='+',
    )


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)
    collections = models.ForeignKey(
        Collection,
        on_delete=models.PROTECT,
    )
    promotions = models.ManyToManyField(
        Promotion,
    )


# customer
#     f_name
#     l_name
#     email(unique)
#     phone
#     birth_date(nullable)

class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Gold'),
        (MEMBERSHIP_GOLD, 'Silver'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(
        max_length=1,
        choices=MEMBERSHIP_CHOICES,
        default=MEMBERSHIP_BRONZE
    )


# Order
#     placed_at (datetime - auto_populated)
#     payment_status
#     P = Pending
#     C = Complete
#     F = Failed

class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS_COMPLETED = 'C'
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_FAILED, 'Failed'),
        (PAYMENT_STATUS_COMPLETED, 'Completed'),
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1,
        choices=PAYMENT_STATUS_CHOICES,
        default=PAYMENT_STATUS_PENDING
    )
    customers = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
    )


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.PROTECT,
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
    )
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
    )


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveSmallIntegerField()

# One-to-Many relationship
#     Collection - Order
#     Customer - Order,
#     Order - Item
#     Cart - Item

# Many-to-Many relationship
