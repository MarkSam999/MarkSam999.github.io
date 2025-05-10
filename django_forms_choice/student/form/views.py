import random
from django.shortcuts import render, redirect
from .forms import MathQuestionForm

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    action_list = ['add', 'subtract','multiply', 'divide']
    action = random.choice(action_list)
    if action == 'add':
        correct_answer = num1 + num2
    if action == 'subtract':
        correct_answer = num1 - num2
        if num2 > num1:

    if action == 'multiply':
        correct_answer = num1 * num2
    if action == 'divide':
        correct_answer = num1 / num2    

    # 3 incorrect variants in radius 10
    wrong_answers = set()
    while len(wrong_answers) < 3:
        fake = correct_answer + random.choice(range(-10, 11))
        if fake != correct_answer and fake >= 0:
            wrong_answers.add(fake)

    # Перемешиваем правильный и неправильные
    all_answers = list(wrong_answers) + [correct_answer]
    random.shuffle(all_answers)
    
    choices = [(str(ans), str(ans)) for ans in all_answers]
    
    return num1, num2, correct_answer, choices, action

def math_question_view(request):
    if request.method == 'POST':
        form = MathQuestionForm(request.POST, choices=request.session.get('choices'))
        if form.is_valid():
            selected = int(form.cleaned_data['answer'])
            correct = request.session.get('correct_answer')
            is_correct = selected == correct
            return render(request, 'result.html', {'is_correct': is_correct, 'correct': correct})
    else:
        num1, num2, correct, choices, action = generate_question()
        form = MathQuestionForm(choices=choices)
        # Сохраняем данные в сессии
        request.session['correct_answer'] = correct
        request.session['choices'] = choices
        return render(request, 'question.html', {'form': form, 'num1': num1, 'num2': num2, 'action': action})
