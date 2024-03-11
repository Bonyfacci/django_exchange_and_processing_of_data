from django.core.management.base import BaseCommand

from producer.models import PurchaseCheck, Product


class Command(BaseCommand):
    help = 'Заполнить БД несколькими чеками'

    def handle(self, *args, **options):
        PurchaseCheck.objects.all().delete()
        purchase_check = [
            {
                "items": [
                    {"product_id": "product_id_1", "quantity": 2, "price": 10.99, "category": "groceries"},
                    {"product_id": "product_id_2", "quantity": 1, "price": 5.49, "category": "electronics"}
                ],
                "transaction_id": "IK558PzAIcoU",
                "timestamp": "2024-02-07T12:34:56",
                "total_amount": 27.47,
                "tax_amount": 2.47,
                "tips_amount": 3.0,
                "payment_method": "credit_card",
                "place_name": "ABC"
            },
            {
                "items": [
                    {"product_id": "product_id_5", "quantity": 2, "price": 10.99, "category": "groceries"},
                    {"product_id": "product_id_6", "quantity": 1, "price": 5.49, "category": "electronics"}
                ],
                "transaction_id": "fFmRfXf5p6Es",
                "timestamp": "2024-02-07T12:34:56",
                "total_amount": 27.47,
                "tax_amount": 2.47,
                "tips_amount": 3.0,
                "payment_method": "credit_card",
                "place_name": "ABCDE"
            }
        ]
        for check in purchase_check:
            check_model = PurchaseCheck.objects.create(
                transaction_id=check.get('transaction_id'),
                timestamp=check.get('timestamp'),
                total_amount=check.get('total_amount'),
                tax_amount=check.get('tax_amount'),
                tips_amount=check.get('tips_amount'),
                payment_method=check.get('payment_method'),
                place_name=check.get('place_name')
            )
            for product in check.get('items'):
                product_model = Product.objects.create(
                    product_id=product.get('product_id'),
                    quantity=product.get('quantity'),
                    price=product.get('price'),
                    category=product.get('category')
                )
                check_model.items.add(product_model)
