from django.db import models
from django.utils.translation import gettext_lazy as _

NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    product_id = models.CharField(_('Product id'), max_length=50, help_text='Уникальный идентификатор товара')
    quantity = models.PositiveIntegerField(_('Quantity'), help_text='Количество товара')
    price = models.DecimalField(_('Price'), max_digits=10, decimal_places=2, help_text='Цена товара')
    category = models.CharField(_('Category'), max_length=50, help_text='Категория товара')

    objects = None

    def __str__(self):
        return f'{self.product_id} - {self.quantity} pcs.'

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        ordering = ('category', 'product_id',)


class PurchaseCheck(models.Model):
    transaction_id = models.CharField(_('Transaction id'), max_length=50, unique=True,
                                      help_text='Уникальный идентификатор транзакции')
    timestamp = models.DateTimeField(_('Timestamp'), help_text='Временная метка совершения покупки')

    items = models.ManyToManyField(Product, related_name='purchase_check_items', help_text='Список товаров в чеке')

    total_amount = models.DecimalField(_('Total amount'), max_digits=10, decimal_places=2, help_text='Общая сумма чека')
    tax_amount = models.DecimalField(_('Tax amount'), max_digits=10, decimal_places=2, help_text='Сумма НДС')
    tips_amount = models.DecimalField(_('Tips amount'), max_digits=10, decimal_places=2, default=0.0,
                                      help_text='Сумма чаевых (если применимо)')

    payment_method = models.CharField(_('Payment method'), max_length=50, help_text='Метод оплаты')

    objects = None

    def __str__(self):
        return f"{self.timestamp} - {self.transaction_id} - {self.total_amount} - {self.payment_method}"

    class Meta:
        verbose_name = _('Purchase receipt')
        verbose_name_plural = _('Purchase receipts')
        ordering = ('-timestamp',)
