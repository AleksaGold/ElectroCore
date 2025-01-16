# Generated by Django 5.1.4 on 2025-01-16 13:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chain", "0002_alter_chain_contact_alter_chain_product"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chain",
            name="contact",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="chain",
                to="chain.contact",
                verbose_name="Контакты",
            ),
        ),
        migrations.AlterField(
            model_name="chain",
            name="product",
            field=models.ManyToManyField(
                related_name="chain", to="chain.product", verbose_name="Продукты"
            ),
        ),
        migrations.AlterField(
            model_name="chain",
            name="supplier",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="chain",
                to="chain.chain",
                verbose_name="Поставщик",
            ),
        ),
    ]
