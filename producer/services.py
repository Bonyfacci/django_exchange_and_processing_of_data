from confluent_kafka import Producer
from django.conf import settings
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder


def send_to_kafka(purchase_check):

    print(f'Начало отправки')

    config = {
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'mygroup',
        'auto.offset.reset': 'earliest'
    }
    serialized_purchase_check = serialize('json', [purchase_check], cls=DjangoJSONEncoder)
    print(serialized_purchase_check)

    producer = Producer(config)

    def delivery_report(err, msg):
        if err is not None:
            print(f'Message delivery failed: {err}')
        else:
            print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

    producer.produce(topic=settings.KAFKA_TOPIC_PREFIX, value=serialized_purchase_check, callback=delivery_report)
    producer.flush()

    print(f'Конец отправки')
