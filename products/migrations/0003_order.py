# Generated by Django 4.1.4 on 2023-01-10 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_shoppingcart_remove_address_user_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                ("order_id", models.IntegerField(primary_key=True, serialize=False)),
                ("order_status", models.CharField(max_length=50)),
                ("order_fulfilled", models.BooleanField(default=False)),
                (
                    "cart",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="products.shoppingcart",
                    ),
                ),
            ],
        ),
    ]
