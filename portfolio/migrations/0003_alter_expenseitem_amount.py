# Generated by Django 4.2.13 on 2024-06-18 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_expenseitem_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenseitem',
            name='amount',
            field=models.FloatField(null=True),
        ),
    ]
