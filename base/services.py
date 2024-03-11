from django.utils.crypto import get_random_string


def generate_id():
    gen_id = get_random_string(length=12)
    return gen_id
