from django.db import models

# Create your models here.


class orders(models.Model):
    order_id = models.TextField(max_length = 50)
    customer_id = models.TextField(max_length = 50)
    payment = models.TextField(max_length = 50)
    order_date = models.TextField(max_length = 50)
    delivery_date = models.TextField(max_length = 50)
