import math
import random


def get_random_numbers():
    """Генерирует 3 случайных числа от 1 до 100"""
    return [random.randint(1, 20) for _ in range(3)]


def lcm(a, b):
    """Вычисляет НОК двух чисел"""
    return a * b // math.gcd(a, b)


def lcm_of_three(a, b, c):
    """Вычисляет НОК трёх чисел"""
    return lcm(lcm(a, b), c)


def play_lcm_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the smallest common multiple of given numbers.")
    
    correct_answers_needed = 3
    correct_answers = 0
    
    while correct_answers < correct_answers_needed:
        numbers = get_random_numbers()
        correct_answer = lcm_of_three(*numbers)
        
        print(f"Question: {' '.join(map(str, numbers))}")
        user_answer = input("Your answer: ")
        
        try:
            user_answer = int(user_answer)
        except ValueError:
            print(f"'{user_answer}' is wrong answer ;(. "
                  "Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
            
        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  "Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    play_lcm_game()