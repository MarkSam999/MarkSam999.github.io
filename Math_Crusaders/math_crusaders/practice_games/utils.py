import random

def generate_example(min_num=1, max_num=10, operations=None):
    if operations is None:
        operations = ['+', '-']  # По умолчанию сложение и вычитание

    # Генерация чисел
    num1 = random.randint(min_num, max_num)
    num2 = random.randint(min_num, max_num)
    # Выбор операции
    operation = random.choice(operations)
    
    if operation == '+':
        question = f"{num1} + {num2}"
        answer = num1 + num2
    elif operation == '-':
        question = f"{num1} - {num2}"
        answer = num1 - num2
    
    return question, answer
