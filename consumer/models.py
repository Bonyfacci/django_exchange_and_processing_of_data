from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import BaseModel, NULLABLE


class Place(BaseModel):
    place_id = models.CharField(_('Place ID'), max_length=50,
                                help_text='Уникальный идентификатор места покупки')
    place_name = models.CharField(_('Place Name'), max_length=150, help_text='Название места покупки')

    objects = None

    def __str__(self):
        return f'{self.place_name} ({self.place_id})'

    class Meta:
        verbose_name = _('Place')
        verbose_name_plural = _('Places')
        ordering = ('place_name',)


class Category(BaseModel):
    name = models.CharField(_('Name'), max_length=50, unique=True, help_text='Название категории товаров')

    objects = None

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ('name',)


class PurchaseInCategory(BaseModel):
    name = models.ForeignKey(Category, max_length=50, on_delete=models.CASCADE, help_text='Название категории')
    price = models.DecimalField(_('Price'), max_digits=10, decimal_places=2, default=0.0,
                                help_text='Цена в категории')

    objects = None

    def __str__(self):
        return f'{self.created} - {self.name} - {self.price}'

    class Meta:
        verbose_name = _('Purchase in category')
        verbose_name_plural = _('Purchases in category')
        ordering = ('name',)


class Purchase(BaseModel):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='purchases', help_text='Место покупки')

    purchase_in_category = models.ManyToManyField(PurchaseInCategory, related_name='purchases_in_category')

    price = models.DecimalField(_('Price'), max_digits=10, decimal_places=2, default=0.0, help_text='Цена покупки')

    tax = models.DecimalField(_('NDS'), max_digits=10, decimal_places=2, default=0.0, help_text='Сумма НДС в чеке')

    tips = models.DecimalField(_('Tips'), max_digits=10, decimal_places=2, default=0.0, help_text='Сумма чаевых в чеке')

    objects = None

    def __str__(self):
        return f'{self.place.place_name} - Purchase #{self.id} - ' \
               f'{self.purchase_in_category.all()}'

    class Meta:
        verbose_name = _('Purchase')
        verbose_name_plural = _('Purchases')
        ordering = ('-id',)


class CategoryAnalytics(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, help_text='Категория товара')

    total_spent = models.DecimalField(_('Total Spent'), max_digits=10, decimal_places=2, default=0.0,
                                      help_text='Общая сумма потраченная на категорию за промежуток времени')
    average_receipt = models.DecimalField(_('Average Receipt'), max_digits=10, decimal_places=2, default=0.0,
                                          help_text='Средний чек по категории')

    objects = None

    def __str__(self):
        return f'Analytics {self.category.name} - {self.total_spent} - {self.average_receipt}'

    class Meta:
        verbose_name = _('Category Analytics')
        verbose_name_plural = _('Category Analytics')
        unique_together = ('category',)


class PurchaseAnalytics(BaseModel):
    place = models.ForeignKey(Place, **NULLABLE, on_delete=models.SET_NULL, help_text='Место покупки')

    total_purchases = models.PositiveIntegerField(_('Total Purchases'), default=0,
                                                  help_text='Общее количество покупок в данном месте')
    total_amount = models.DecimalField(_('Total Amount'), max_digits=10, decimal_places=2, default=0.0,
                                       help_text='Общая стоимость покупок')

    average_receipt = models.DecimalField(_('Average Receipt'), max_digits=10, decimal_places=2, default=0.0,
                                          help_text='Средний чек в данном месте')

    total_nds = models.DecimalField(_('Total NDS'), max_digits=10, decimal_places=2, default=0.0,
                                    help_text='Общая сумма НДС за промежуток времени')
    total_tips = models.DecimalField(_('Total Tips'), max_digits=10, decimal_places=2, default=0.0,
                                     help_text='Общая сумма чаевых за промежуток времени')

    category_analytics = models.ManyToManyField(CategoryAnalytics, related_name='category_analytics')

    objects = None

    def __str__(self):
        return f'{self.place.place_name} - Purchase Analytics'

    class Meta:
        verbose_name = _('Purchase analytics')
        verbose_name_plural = _('Purchases analytics')


class OverallAnalytics(BaseModel):
    purchase_analytics = models.ManyToManyField(PurchaseAnalytics, related_name='purchase_analytics')

    objects = None

    def __str__(self):
        return f'{self.created} - {self.purchase_analytics} - Overall Analytics'

    class Meta:
        verbose_name = _('Overall Analytics')
        verbose_name_plural = _('Overall Analytics')
