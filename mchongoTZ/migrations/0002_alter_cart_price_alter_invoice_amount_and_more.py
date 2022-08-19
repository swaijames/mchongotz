# Generated by Django 4.1 on 2022-08-16 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mchongoTZ', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='invoicedata',
            name='item_cost',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='invoicedata',
            name='quantity',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='product',
            name='p_price',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
