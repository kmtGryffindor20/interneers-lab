from django.db import migrations


def migrate_string_categories_to_references(apps, schema_editor):
    """
    Backfill ProductDocument.category from legacy string values to ProductCategory references.

    This migration is idempotent:
    - existing ProductCategory documents are reused by name
    - only products with string categories are updated
    """
    from products.models import ProductCategory, ProductDocument

    product_collection = ProductDocument._get_collection()
    # Read only legacy category strings directly from MongoDB to avoid
    # deserialization issues when mixed types exist in the same field.
    category_names = product_collection.distinct(
        "category", {"category": {"$type": "string"}}
    )

    for raw_name in category_names:
        category_name = (raw_name or "").strip()
        if not category_name:
            continue

        category_doc = ProductCategory.objects(name=category_name).first()  # type: ignore[attr-defined]
        if not category_doc:
            category_doc = ProductCategory(name=category_name)
            category_doc.save()

        # Use the DB representation of category_id to match how mongoengine stores UUIDs.
        mongo_id = category_doc.to_mongo()["_id"]

        product_collection.update_many(
            {"category": raw_name},
            {"$set": {"category": mongo_id}},
        )


def noop_reverse(apps, schema_editor):
    # Irreversible data migration: category strings are replaced by references.
    pass


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.RunPython(migrate_string_categories_to_references, noop_reverse),
    ]
