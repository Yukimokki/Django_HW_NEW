from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from users.forms import UserRegisterForm
from users.models import CustomUser
from config.settings import EMAIL_HOST_USER

import secrets
import random
import string


class UserLoginView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return redirect(reverse("catalog:home"))

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))

class UserCreateView(CreateView):
    model = CustomUser
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """ sends email to the new user for confirmation"""
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token=token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}'
        send_mail(
            subject="Confirm your email for Skystore registration",
            message=f"Hello! To complete your registration, please, confirm your email to confirm your email {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


def email_verification(request, token):
    """ verifies token and activate user profile"""
    user = get_object_or_404(CustomUser, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


def generate_random_password(length=8):
    """ generates random password """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(length):
        random_char = random.choice(characters)
        password += random_char

    return password

def reset_password(request):
    """ Updates password if forgotten"""
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = CustomUser.objects.get(email=email)
            new_password = generate_random_password()
            user.password = make_password(new_password)
            user.save()

            send_mail(
                subject="New Skystore password",
                message=f"your new password is {new_password}\n",
                from_email=EMAIL_HOST_USER,
                recipient_list=[user.email],
                fail_silently=False,
            )

            return redirect('users:login')

        except CustomUser.DoesNotExist:
            return render(request, 'users/password_reset.html', {'error':'This email is not found!'})

    return render(request, 'users/password_reset.html')
