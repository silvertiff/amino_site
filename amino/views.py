from django.shortcuts import render, redirect, get_object_or_404
from .models import AminoAcid
from .forms import AminoAcidForm, QuizForm
import random

def acid_list(request):
    acids = AminoAcid.objects.all()
    return render(request, 'amino/acid_list.html', {'acids': acids})

def add_acid(request):
    if request.method == 'POST':
        form = AminoAcidForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('acid_list')
    else:
        form = AminoAcidForm()
    return render(request, 'amino/add_acid.html', {'form': form})


def flashcard(request):
    acid_id = request.GET.get('acid_id')
    show_back = request.GET.get('show_back') == '1'

    if acid_id:
        acid = get_object_or_404(AminoAcid, id=acid_id)
    else:
        acid = random.choice(AminoAcid.objects.all())

    return render(request, 'amino/flashcard.html', {'acid': acid, 'show_back': show_back})


import random
from django.shortcuts import render, get_object_or_404
from .models import AminoAcid
from .forms import QuizForm

def quiz(request):
    # Определяем тип вопроса: по умолчанию случайный
    question_type = request.GET.get('type')
    if not question_type:
        question_type = random.choice(['name', 'structure'])

    if request.method == 'POST':
        acid_id = request.POST.get('acid_id')
        question_type = request.POST.get('question_type')
        acid = get_object_or_404(AminoAcid, id=acid_id)
        form = QuizForm(request.POST)
        if form.is_valid():
            answer = form.cleaned_data['answer'].strip().lower()
            if question_type == 'name':
                correct = answer == acid.three_letter_code.lower() or answer == acid.one_letter_code.lower()
            else:  # structure
                correct = answer == acid.name.lower()
            return render(request, 'amino/quiz_result.html', {
                'acid': acid,
                'answer': answer,
                'correct': correct,
                'question_type': question_type,
            })
        return render(request, 'amino/quiz.html', {'acid': acid, 'form': form, 'question_type': question_type})
    else:
        acid = random.choice(AminoAcid.objects.all())
        form = QuizForm()
        return render(request, 'amino/quiz.html', {'acid': acid, 'form': form, 'question_type': question_type})
