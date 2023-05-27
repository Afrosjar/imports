import random
from data import name
from rich import print


def get_employees():
    print('Выводим информацию для: ',random.choice(name), ":house:")

