from django.shortcuts import render
from .forms import AnswerForm
from .utils import generate_example

def play_game(request):
    if 'question' not in request.session:
        question, correct_answer = generate_example()
        request.session['question'] = question
        request.session['correct_answer'] = correct_answer
    else:
        question = request.session['question']
        correct_answer = request.session['correct_answer']

    result = None
    score = 0

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            user_answer = form.cleaned_data['user_answer']
            if user_answer == correct_answer:
                result = 'Correct!'
                score = 1
            else:
                result = f'Incorrect. It is {correct_answer}'
            # Сбрасываем текущий пример
            del request.session['question']
            del request.session['correct_answer']
            form = AnswerForm()  # Очищаем форму
    else:
        form = AnswerForm()

    return render(request, 'play.html', {
        'question': question,
        'form': form,
        'result': result,
        'score': score,
    })

