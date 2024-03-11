import json

from confluent_kafka import Consumer, KafkaException
from django.conf import settings

from consumer.utils import process_receipt


def receive_from_kafka():

    print(f'\nПриём!')

    config = {
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'mygroup',
        'auto.offset.reset': 'earliest'
    }

    consumer = Consumer(config)

    consumer.subscribe([settings.KAFKA_TOPIC_PREFIX])

    try:
        while True:
            msg = consumer.poll(timeout=1.0)

            if msg is None:
                continue
            if msg.error():
                raise KafkaException(msg.error())

            try:
                # print("Подключение к Topic: {} and Partition : {}".format(msg.topic(), msg.partition()))
                # print("Получено сообщение: {} with Offset : {}".format(msg.value().decode('utf-8'), msg.offset()))

                purchase_check_json = json.loads(msg.value().decode('utf-8'))
                purchase_check_data = purchase_check_json[0]["fields"]

                process_receipt(purchase_check_data)

            except Exception as e:
                print(f"Ошибка обработки сообщения: {str(e)}")

    except KeyboardInterrupt:
        pass
    finally:
        print('Конец сессии')
        consumer.close()
