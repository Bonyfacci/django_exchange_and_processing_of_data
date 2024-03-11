import datetime
import logging

from celery import shared_task

from consumer.utils import create_overall_analytics

logger = logging.getLogger(__name__)


@shared_task
def create_analytics():
    current_time = datetime.datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
    print(f'Время сервера: {current_time}')

    logger.info(f"Создание аналитики покупок")

    logger.info(f"Получаем данные о покупках и анализируем")
    create_overall_analytics()
    logger.info(f"Записываем в базу данных")
    logger.info(f"Данные успешно обновлены")
