# Generated by Django 4.2.13 on 2024-06-18 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenseitem',
            name='amount',
            field=models.PositiveBigIntegerField(default=0, null=True),
        ),
    ]
