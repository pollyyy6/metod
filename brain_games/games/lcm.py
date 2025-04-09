import math
import random


DESCRIPTION = "Find the smallest common multiple of given numbers."


def get_random_numbers():
    """Генерирует 3 случайных числа от 1 до 100"""
    return [random.randint(1, 20) for _ in range(3)]


def lcm(a, b):
    """Вычисляет НОК двух чисел"""
    return a * b // math.gcd(a, b)


def lcm_of_three(a, b, c):
    """Вычисляет НОК трёх чисел"""
    return lcm(lcm(a, b), c)


def generate_round():
    numbers = get_random_numbers()
    question = " ".join(map(str, numbers))
    correct_answer = str(lcm_of_three(*numbers))
    return question, correct_answer