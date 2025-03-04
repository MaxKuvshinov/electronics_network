# Generated by Django 5.1.6 on 2025-02-26 13:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0002_rename_create_at_networknode_created_at"),
        ("product", "0002_alter_product_release_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="network_node",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product",
                to="network.networknode",
                verbose_name="Участник сети",
            ),
        ),
    ]
