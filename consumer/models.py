from django.db import models
from django.utils.translation import gettext_lazy as _


class Place(models.Model):
    place_id = models.CharField(_('Place ID'), max_length=50, unique=True,
                                help_text='Уникальный идентификатор места покупки')
    place_name = models.CharField(_('Place Name'), max_length=150, help_text='Название места покупки')

    def __str__(self):
        return f'{self.place_name} ({self.place_id})'

    class Meta:
        verbose_name = _('Place')
        verbose_name_plural = _('Places')
        ordering = ('place_name',)


class Category(models.Model):
    name = models.CharField(_('Name'), max_length=50, unique=True, help_text='Название категории товаров')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ('name',)


class Purchase(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='purchases', help_text='Место покупки')
    total_purchases = models.PositiveIntegerField(_('Total Purchases'), default=0,
                                                  help_text='Общее количество покупок в данном месте')
    average_receipt = models.DecimalField(_('Average Receipt'), max_digits=10, decimal_places=2, default=0.0,
                                          help_text='Средний чек в данном месте')
    total_nds = models.DecimalField(_('Total NDS'), max_digits=10, decimal_places=2, default=0.0,
                                    help_text='Общая сумма НДС за промежуток времени')
    total_tips = models.DecimalField(_('Total Tips'), max_digits=10, decimal_places=2, default=0.0,
                                     help_text='Общая сумма чаевых за промежуток времени')

    def __str__(self):
        return f'{self.place.place_name} - Purchase #{self.id}'

    class Meta:
        verbose_name = _('Purchase')
        verbose_name_plural = _('Purchases')
        ordering = ('-id',)


class CategoryAnalytics(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name='category_analytics',
                                 help_text='Покупка')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, help_text='Категория товара')
    total_spent = models.DecimalField(_('Total Spent'), max_digits=10, decimal_places=2, default=0.0,
                                      help_text='Общая сумма потраченная на категорию за промежуток времени')
    average_receipt = models.DecimalField(_('Average Receipt'), max_digits=10, decimal_places=2, default=0.0,
                                          help_text='Средний чек по категории')

    def __str__(self):
        return f'{self.purchase.place.place_name} - {self.category.name} Analytics'

    class Meta:
        verbose_name = _('Category Analytics')
        verbose_name_plural = _('Category Analytics')
        unique_together = ('purchase', 'category')


class OverallAnalytics(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True, related_name='overall_analytics',
                                 help_text='Место покупки')
    total_purchases = models.PositiveIntegerField(_('Total Purchases'), default=0,
                                                  help_text='Общее количество покупок в данном месте')
    average_receipt = models.DecimalField(_('Average Receipt'), max_digits=10, decimal_places=2, default=0.0,
                                          help_text='Средний чек в данном месте')

    def __str__(self):
        return f'{self.place.place_name} - Overall Analytics'

    class Meta:
        verbose_name = _('Overall Analytics')
        verbose_name_plural = _('Overall Analytics')
