from django.shortcuts import render
from django import forms
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.utils import timezone
from users.forms import MessageForm
from django.shortcuts import render, redirect
from .models import Message
from django.views.generic import (ListView, 
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView
)



def chats_view(request):
    
    form = MessageForm()

    if request.method == 'POST' and 'create_message' in request.POST:
        form = MessageForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                chat_message = form.save(commit=False)
                chat_message.posted_by = request.user
                chat_message.save()
            else:
                return redirect('login')
        else:
            return redirect('home')
        
    chat_messages = Message.objects.all().order_by('-publish_date')
    paginator = Paginator(chat_messages, 3) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'chats/chats.html', {
        'form': form,
        'chat_messages': chat_messages and page_obj,
    })