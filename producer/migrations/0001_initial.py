# Generated by Django 5.0.3 on 2024-03-06 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(help_text='Уникальный идентификатор товара', max_length=50, verbose_name='Product id')),
                ('quantity', models.PositiveIntegerField(help_text='Количество товара', verbose_name='Quantity')),
                ('price', models.DecimalField(decimal_places=2, help_text='Цена товара', max_digits=10, verbose_name='Price')),
                ('category', models.CharField(help_text='Категория товара', max_length=50, verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ('category', 'product_id'),
            },
        ),
        migrations.CreateModel(
            name='PurchaseCheck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(help_text='Уникальный идентификатор транзакции', max_length=50, unique=True, verbose_name='Transaction id')),
                ('timestamp', models.DateTimeField(help_text='Временная метка совершения покупки', verbose_name='Timestamp')),
                ('total_amount', models.DecimalField(decimal_places=2, help_text='Общая сумма чека', max_digits=10, verbose_name='Total amount')),
                ('tax_amount', models.DecimalField(decimal_places=2, help_text='Сумма НДС', max_digits=10, verbose_name='Tax amount')),
                ('tips_amount', models.DecimalField(decimal_places=2, default=0.0, help_text='Сумма чаевых (если применимо)', max_digits=10, verbose_name='Tips amount')),
                ('payment_method', models.CharField(help_text='Метод оплаты', max_length=50, verbose_name='Payment method')),
                ('items', models.ManyToManyField(help_text='Список товаров в чеке', related_name='purchase_check_items', to='producer.product')),
            ],
            options={
                'verbose_name': 'Purchase receipt',
                'verbose_name_plural': 'Purchase receipts',
                'ordering': ('-timestamp',),
            },
        ),
    ]
