# Generated by Django 5.1.4 on 2024-12-25 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_orders_customer_orders_product"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name="orders",
            name="tag",
            field=models.ManyToManyField(to="accounts.tag"),
        ),
    ]
