from django.shortcuts import render

def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
    return render({'form': form})
