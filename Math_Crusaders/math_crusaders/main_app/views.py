from django.shortcuts import render
from django.http import HttpResponse

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

news_posts = [
    {   
        'topic': 'The game has reached 1000 users',
        'article': 'Today Math Crusaders has over 1000 registered users',
        'post_date_posted': 'September 2, 2024',
    }
]

comments = [
    {
        'author': 'User82792',
        'comment': 'Oh, this is good!',
        'comment_date_posted': 'September 7, 2024',
    },
    {
        'author': 'User52723',
        'comment': 'Hmm it is so fast',
        'comment_date_posted': 'September 11, 2024',
    }
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
        'hist_events': hist_events
    }
    return render(request, 'main_app/history.html', context)

def news(request):
    context = {
        'news_posts': news_posts,
        'comments': comments
    }
    return render(request, 'main_app/news.html', context)