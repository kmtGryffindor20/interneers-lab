import uuid
from mongoengine import (
    Document,
    StringField,
    DecimalField,
    IntField,
    UUIDField,
    DateTimeField,
    ReferenceField,
    NULLIFY,
)
from mongoengine.signals import pre_save
from datetime import datetime, timezone


class ProductCategory(Document):
    category_id = UUIDField(primary_key=True, default=uuid.uuid4)
    name = StringField(max_length=255, required=True)
    description = StringField()
    created_at = DateTimeField(default=datetime.now(timezone.utc))
    updated_at = DateTimeField(default=datetime.now(timezone.utc))

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_at = datetime.now(timezone.utc)


class ProductDocument(Document):
    product_id = UUIDField(primary_key=True, default=uuid.uuid4)
    name = StringField(max_length=255, required=True)
    description = StringField()
    category = ReferenceField(ProductCategory, reverse_delete_rule=NULLIFY)
    price = DecimalField(max_digits=10, decimal_places=2, required=True)
    brand = StringField(max_length=255, required=True)
    quantity = IntField(required=True)
    created_at = DateTimeField(default=datetime.now(timezone.utc))
    updated_at = DateTimeField(default=datetime.now(timezone.utc))

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_at = datetime.now(timezone.utc)


pre_save.connect(ProductDocument.pre_save, sender=ProductDocument)
pre_save.connect(ProductCategory.pre_save, sender=ProductCategory)
