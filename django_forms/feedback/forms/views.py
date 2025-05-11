from django.shortcuts import render

def feedback(request):
    if request.method == "POST":
        form = FeedbackForm
    return render({'form': form})
