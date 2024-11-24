from django.shortcuts import render
from .models import News_Post
from .models import Hist_Event

hist_events = [
    {
        'hist_topic': 'The creation of the game',
        'hist_article': 'The game was created in 2024',
    }
]

qa_main = [
    {
        'question': 'Who created this game and when?',
        'answer': 'This game was created by ___ Studios',
    },
    {
        'question': 'How to learn new math skills?',
        'answer': 'Go to practice page and find lessons you did not pass yet.',
    }
]

levels = [
    {
        'level': '1',
        'lev_def': 'Intro to Math',
    },
    {
        'level': '2',
        'lev_def': 'Intro to Addition',
    },
    {
        'level': '3',
        'lev_def': 'Addition Practice',
    },
    {
        'level': '4',
        'lev_def': 'Addition Test 1',
    },
]

map_def = [
    {'map_def_content': 'The map with a lot of different levels',}
]

def welcome(request):
    return render(request, 'main_app/welcome.html')

def home(request):
    return render(request, 'main_app/home.html')

def about(request):
    context = {
        'qa_main': qa_main
    }
    return render(request, 'main_app/about.html', context)

def history(request):
    context = {
        'hist_events': Hist_Event.objects.all()
    }
    return render(request, 'main_app/history.html', context)

def news(request):
    context = {
        'news_posts': News_Post.objects.all()
    }
    return render(request, 'main_app/news.html', context)

def game_map(request):
    context = {
        'levels': levels,
        'map_def': map_def,
    }
    return render(request, 'main_app/game_map.html', context)

def statistics(request):
    context = {}
    return render(request, 'main_app/statistics.html', context)

def chat(request):
    context = {}
    return render(request, 'main_app/chat.html', context)