from django.db import models

CATEGORY_CHOICES = (
    ('CR', 'Curd'),
    ('ML', 'Milkshake'),
    ('PA', 'Paneer'),
    ('IC', 'Icecream'),
    ('GH', 'Ghee'),
    ('CH', 'Cheese'),
    ('LS', 'Lassi'),
    ('MK', 'Milk'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)  # Specify max_length
    composition = models.CharField(max_length=500)  # Specify max_length
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.title
