import random


DESCRIPTION = 'What number is missing in the progression?'


def generate_geometric_progression(start, ratio, length):
    return [start * ratio ** i for i in range(length)]


def generate_round():
    start = random.randint(1, 5)
    ratio = random.randint(2, 5)
    length = random.randint(5, 10)
    hidden_index = random.randint(0, length - 1)
    
    progression = generate_geometric_progression(start, ratio, length)
    correct_answer = str(progression[hidden_index])
    
    progression_str = []
    for i, num in enumerate(progression):
        if i == hidden_index:
            progression_str.append('..')
        else:
            progression_str.append(str(num))
    
    question = ' '.join(progression_str)
    
    return question, correct_answer