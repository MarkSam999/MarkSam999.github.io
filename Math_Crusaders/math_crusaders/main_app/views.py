from django.shortcuts import render
from django import forms
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from users.forms import NewsPostForm
from users.models import Profile
from django.views.generic import (ListView, 
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView
)
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

def arena(request):
    return render(request, 'main_app/arena.html')

def rating(request):
    context = {
        'profiles': Profile.objects.all()
    }
    return render(request, 'main_app/rating.html', context)

class RatingListView(ListView):
    model = Profile
    template_name = 'main_app/rating.html'
    context_object_name = 'profiles'
    ordering = ['-rating']
    paginate_by = 1

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

class NewsPostListView(ListView):
    model = News_Post
    template_name = 'main_app/news.html'
    context_object_name = 'news_posts'
    ordering = ['-publish_date']
    paginate_by = 2

class NewsPostDetailView(DetailView):
    model = News_Post
    template_name = 'main_app/news_post.html'

class NewsPostCreateView(CreateView):
    model = News_Post
    form_class = NewsPostForm
    widgets = {
            'content': forms.Textarea(attrs={
                'style': 'resize: none; width: 100%; place-self: center;'
            }),
        }
    template_name = 'main_app/news_post_add.html'
    success_url = reverse_lazy('news')

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)
class NewsPostUpdateView(UserPassesTestMixin, UpdateView):
    model = News_Post
    form_class = NewsPostForm
    widgets = {
            'content': forms.Textarea(attrs={
                'style': 'resize: none; width: 100%; place-self: center;'
            }),
        }
    template_name = 'main_app/news_post_add.html'
    success_url = reverse_lazy('news') 

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)    
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.posted_by:
            return True
        return False

class NewsPostDeleteView(UserPassesTestMixin, DeleteView):
    model = News_Post
    template_name = 'main_app/news_post_delete.html'
    success_url = reverse_lazy('news') 

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.posted_by:
            return True
        return False

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