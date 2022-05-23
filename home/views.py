from django.shortcuts import render
from django.core.mail import send_mail
from .models import Feedback


def index(request):
    return render(request, 'home/index.html')


def contact(request):
    if request.method == 'GET':
        return render(request, 'home/contact.html')
    elif request.method == 'POST':
        feedback = Feedback()
        feedback.name = request.POST.get('name')
        feedback.user_email = request.POST.get('email')
        feedback.subject = request.POST.get('subject')
        feedback.message = request.POST.get('message')
        feedback.save()

        send_mail(feedback.user_email, feedback.message, feedback.name, ['grine1108@gmail.com'], fail_silently=False)
        return render(request, 'home/success.html')


def success(request):
    return render(request, 'home/success.html')


def about(request):
    return render(request, 'home/about.html')