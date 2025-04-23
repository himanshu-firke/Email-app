from django.shortcuts import render
from django.core.mail import send_mail
from .forms import EmailForm
from django.contrib import messages

def send_email(request):
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            recipient = form.cleaned_data["recipient"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]

            send_mail(subject, message, 'himanshufirke04@gmail.com', [recipient])

            messages.success(request, "Email sent successfully!")
    else:
        form = EmailForm()
    
    return render(request, "emailapp/send_email.html", {"form": form})
