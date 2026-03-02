from django.db import models
from .validators import validate_positive
import uuid


class Product(models.Model):

    product_id = models.UUIDField(
        primary_key=True, editable=False, help_text="Unique identifier for the product", default=uuid.uuid4
    )
    name = models.CharField(
        max_length=255, db_index=True, help_text="The name of the product"
    )
    description = models.TextField(
        blank=True, help_text="A detailed description of the product"
    )
    category = models.CharField(
        max_length=255, db_index=True, help_text="The category of the product"
    )  # Could possibly be another model with a ForeignKey relationship
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="The price of the product",
        validators=[validate_positive],
    )
    brand = models.CharField(
        max_length=255, db_index=True, help_text="The brand of the product"
    )  # Could possibly be another model with a ForeignKey relationship
    quantity = models.PositiveIntegerField(
        help_text="The available quantity of the product",
        validators=[validate_positive],
    )
