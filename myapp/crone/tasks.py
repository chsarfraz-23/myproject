from django.db.models import Q

from MyProject import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from myapp.models import User


def my_crone_task():
    query = Q(username="sarfraz")
    profile_data = User.objects.filter(query).first()

    subject = "Account Verification"
    html_message = render_to_string(
        "verification.html",
        context={"name": profile_data.username},
        )
    message = EmailMultiAlternatives(
        subject=subject,
        body=html_message,
        from_email=settings.EMAIL_HOST_USER,
        to=[profile_data.email],
    )
    message.attach_alternative(html_message, "text/html")
    message.send()

