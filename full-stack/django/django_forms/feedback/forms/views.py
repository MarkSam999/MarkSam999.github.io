from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review

def feedback(request):
    if request.method == "POST" and 'form':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review_list')
    else:
        form = ReviewForm()
    return render(request, "add_review.html", {'form': form})

def reviews(request):
    context = {
        'reviews': Review.objects.all()
    }

    return render(request, "all_reviews.html", context)
