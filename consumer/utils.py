from consumer.models import Place, Category, PurchaseInCategory, Purchase, OverallAnalytics, PurchaseAnalytics, \
    CategoryAnalytics
from producer.models import Product


def get_product_id(product_id):
    product = Product.objects.get(pk=product_id)
    return product


def get_category_id(category_name):
    category = Category.objects.get(name=category_name)
    return category


def process_receipt(receipt_data):
    # Извлечение данных из чека
    transaction_id = receipt_data.get('transaction_id')
    timestamp = receipt_data.get('timestamp')
    total_amount = receipt_data.get('total_amount')
    tax_amount = receipt_data.get('tax_amount')
    tips_amount = receipt_data.get('tips_amount')
    payment_method = receipt_data.get('payment_method')
    place_name = receipt_data.get('place_name')

    items_data = receipt_data.get('items')

    # Получение или создание объекта Place
    place, created = Place.objects.get_or_create(
        place_id=place_name,
        place_name=place_name
    )
    if created:
        print(f'Создано новое место: {place}')

    # Создание объекта Purchase
    purchase = Purchase.objects.create(
        place=place,
        price=total_amount,
        tax=tax_amount,
        tips=tips_amount,
    )

    # Получение или создание объекта Category и PurchaseInCategory
    for product_id in items_data:
        product = get_product_id(product_id)
        category, created = Category.objects.get_or_create(
            name=product.category,
        )
        if created:
            print(f'Создано новая категория: {product.category}')

        category_id = get_category_id(product.category)

        # Создание объекта PurchaseInCategory
        purchase_in_category = PurchaseInCategory.objects.create(
            name=category_id,
            price=product.price * product.quantity
        )

        print(f'Покупка в категории {purchase_in_category} создана')

        purchase.purchase_in_category.add(purchase_in_category)

    print(purchase)


def create_overall_analytics():

    overall_analytics = OverallAnalytics.objects.create()

    for purchase in Purchase.objects.all():
        place = purchase.place
        purchase_in_category = purchase.purchase_in_category.all()
        price = purchase.price
        tax = purchase.tax
        tips = purchase.tips

        purchase_analytics, purchase_analytics_created = PurchaseAnalytics.objects.get_or_create(
            place=place,
            total_amount=price,
            total_purchases=1,
            average_receipt=price / 1,
            total_nds=tax,
            total_tips=tips,
        )

        if not purchase_analytics_created:
            purchase_analytics.total_purchases += 1
            purchase_analytics.total_amount += price
            purchase_analytics.average_receipt = purchase_analytics.average_receipt / purchase_analytics.total_amount
            purchase_analytics.total_nds += tax
            purchase_analytics.total_tips += tips

            category_grouped_data = {}

            for item in purchase_in_category:
                name = item.name
                price = item.price

                if name in category_grouped_data:
                    category_grouped_data[name].append(price)
                else:
                    category_grouped_data[name] = [price]

            for category_name, price in category_grouped_data.items():

                category = Category.objects.get(name=category_name)

                category_analytics, category_analytics_created = CategoryAnalytics.objects.update_or_create(
                    category=category,
                    total_spent=sum(price),
                    average_receipt=sum(price)/len(price)
                )

                if not category_analytics_created:
                    print(category_analytics)

                purchase_analytics.category_analytics.add(category_analytics)
        else:
            category_grouped_data = {}

            for item in purchase_in_category:
                name = item.name
                price = item.price

                if name in category_grouped_data:
                    category_grouped_data[name].append(price)
                else:
                    category_grouped_data[name] = [price]

            for category_name, price in category_grouped_data.items():

                category = Category.objects.get(name=category_name)

                category_analytics, category_analytics_created = CategoryAnalytics.objects.update_or_create(
                    category=category,
                    total_spent=sum(price),
                    average_receipt=sum(price) / len(price)
                )

                if not category_analytics_created:
                    print(category_analytics)

                purchase_analytics.category_analytics.add(category_analytics)

        for item in PurchaseAnalytics.objects.all():
            overall_analytics.purchase_analytics.add(item)
