from django.contrib.auth import authenticate, login, logout, \
    update_session_auth_hash

from django.utils.encoding import force_bytes, force_str

from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .forms import (
    LoginForm,
    LoginEmailForm,
    LoginEmailOrUsernameForm,
    RegistrationForm,
    ResetPasswordEmailForm,
    ResendActivationForm,
    ChangePasswordForm,
    ChangeEmailForm,
    ChangeProfileForm
)
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth.forms import SetPasswordForm
from django.contrib import messages

User = get_user_model()


def reset_password_confirm(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,
                                 'Your password has been reset. You can now log in with your new password.')
                return redirect('account:login')
        else:
            form = SetPasswordForm(user)

        context = {'form': form}
        return render(request, 'accounts/reset_password_confirm.html',
                      context)
    else:
        messages.error(request, 'Invalid password reset link.')
        return redirect('accounts:login')


class PasswordResetConfirmView(FormView):
    template_name = 'accounts/reset_password_confirm.html'
    form_class = SetPasswordForm
    success_url = reverse_lazy('accounts:login')

    def get_user(self, uidb64):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            return User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        uidb64 = self.kwargs.get('uidb64')
        token = self.kwargs.get('token')
        context['valid_link'] = self.get_user(
            uidb64) and default_token_generator.check_token(
            self.get_user(uidb64), token)
        return context

    def form_valid(self, form):
        uidb64 = self.kwargs.get('uidb64')
        token = self.kwargs.get('token')
        user = self.get_user(uidb64)
        if user and default_token_generator.check_token(user, token):
            form.save()
            messages.success(self.request,
                             'Your password has been reset. You can now log in with your new password.')
        else:
            messages.error(self.request, 'Invalid password reset link.')
        return super().form_valid(form)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data['username_or_email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username_or_email,
                                password=password)
            if user is not None:
                login(request, user)
                return redirect(
                    'accounts-1:profile')  # Replace 'profile' with the actual profile URL name
            else:
                form.add_error(None, 'Invalid credentials')
    else:
        form = LoginForm()

    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def login_email_view(request):
    if request.method == 'POST':
        form = LoginEmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(
                    'accounts-1:profile')  # Replace 'profile' with the actual profile URL name
            else:
                form.add_error(None, 'Invalid credentials')
    else:
        form = LoginEmailForm()

    context = {'form': form}
    return render(request, 'accounts/login_email.html', context)


def login_email_or_username_view(request):
    if request.method == 'POST':
        form = LoginEmailOrUsernameForm(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data['username_or_email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username_or_email,
                                password=password) or \
                   authenticate(request, email=username_or_email,
                                password=password)
            if user is not None:
                login(request, user)
                return redirect(
                    'accounts-1:profile')  # Replace 'profile' with the actual profile URL name
            else:
                form.add_error(None, 'Invalid credentials')
    else:
        form = LoginEmailOrUsernameForm()

    context = {'form': form}
    return render(request, 'accounts/login_email_or_username.html', context)


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # User needs to activate the accounts-1 via email
            user.save()
            # Send activation email here
            return render(request, 'accounts/registration_complete.html')
    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'accounts/registration.html', context)


def logout_view(request):
    logout(request)
    return redirect(
        'accounts:login')  # Replace 'login' with the actual login URL name


@login_required
def profile_activation_email_view(request):
    user = request.user
    current_site = get_current_site(request)
    subject = 'Activate Your Profile'
    message = render_to_string('accounts/profile_activation_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': default_token_generator.make_token(user),
    })
    user.email_user(subject, message)
    return render(request, 'accounts/profile_activation_email_sent.html')


def activate_profile(request, activation_key):
    try:
        user_id = force_str(urlsafe_base64_decode(activation_key))
        user = CustomUser.objects.get(pk=user_id)
        if user.is_active:
            return render(request,
                          'accounts/profile_activation_complete.html')
        user.is_active = True
        user.save()
        return render(request, 'accounts/profile_activation_complete.html')
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        return render(request, 'accounts/invalid_activation_link.html')


def reset_password_email_view(request):
    if request.method == 'POST':
        form = ResetPasswordEmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = CustomUser.objects.get(email=email)
            current_site = get_current_site(request)
            subject = 'Reset Your Password'
            message = render_to_string('accounts/reset_password_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            user.email_user(subject, message)
            return render(request, 'accounts/reset_password_email_sent.html')
    else:
        form = ResetPasswordEmailForm()

    context = {'form': form}
    return render(request, 'accounts/reset_password_email.html', context)


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/reset_password_confirm.html'
    success_url = reverse_lazy('accounts-1:password_reset_complete')
    token_generator = default_token_generator
    post_reset_login = True

    def get_user(self, uidb64):
        User = get_user_model()
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            return User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return None


def resend_activation_view(request):
    if request.method == 'POST':
        form = ResendActivationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = CustomUser.objects.get(email=email)
            current_site = get_current_site(request)
            subject = 'Activate Your Profile'
            message = render_to_string(
                'accounts/profile_activation_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
                })
            user.email_user(subject, message)
            return render(request,
                          'accounts/profile_activation_email_sent.html')
    else:
        form = ResendActivationForm()

    context = {'form': form}
    return render(request, 'accounts/resend_activation.html', context)


@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request,
                             'Your password was successfully updated!')
            return redirect(
                'accounts-1:profile')  # Replace 'profile' with the actual profile URL name
    else:
        form = ChangePasswordForm(request.user)

    context = {'form': form}
    return render(request, 'accounts/change_password.html', context)


@login_required
def change_email_view(request):
    if request.method == 'POST':
        form = ChangeEmailForm(request.user, request.POST)
        if form.is_valid():
            new_email = form.cleaned_data['new_email']
            user = request.user
            user.email = new_email
            user.is_active = False  # User needs to reconfirm new email
            user.save()

            current_site = get_current_site(request)
            subject = 'Activate Your New Email'
            message = render_to_string('accounts/email_change_request.html', {
                'user': user,
                'new_email': new_email,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            user.email_user(subject, message)
            messages.success(request,
                             'An email with activation link has been sent to your')


@login_required
def change_profile_view(request):
    if request.method == 'POST':
        form = ChangeProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Your profile information was successfully updated!')
            return redirect(
                'accounts-1:profile')  # Replace 'profile' with the actual profile URL name
    else:
        form = ChangeProfileForm(instance=request.user)

    context = {'form': form}
    return render(request, 'accounts/change_profile.html', context)


@login_required
def profile_view(request):
    user = request.user
    context = {'user': user}
    return render(request, 'accounts/profile.html', context)


@login_required
def resend_activation_view(request):
    if request.method == 'POST':
        form = ResendActivationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = CustomUser.objects.get(email=email)
            current_site = get_current_site(request)
            subject = 'Activate Your Profile'
            message = render_to_string(
                'accounts/profile_activation_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
                })
            user.email_user(subject, message)
            return render(request,
                          'accounts/profile_activation_email_sent.html')
    else:
        form = ResendActivationForm()

    context = {'form': form}
    return render(request, 'accounts/resend_activation.html', context)


@login_required
def delete_profile_confirm_view(request):
    return render(request, 'accounts/delete_profile_confirm.html')


@login_required
def delete_profile_complete_view(request):
    user = request.user
    user.delete()
    return render(request, 'accounts/delete_profile_complete.html')


@login_required
def delete_profile_cancel_view(request):
    return render(request, 'accounts/delete_profile_cancel.html')


@login_required
def generate_api_key_view(request):
    if request.method == 'POST':
        user = request.user
        if user.api_key:
            return render(request, 'accounts/api_key_already_generated.html')
        api_key = CustomUser.objects.generate_api_key()
        user.api_key = api_key
        user.save()
        return render(request, 'accounts/api_key_generation_complete.html',
                      {'api_key': api_key})
    return render(request, 'accounts/api_key_generation.html')


def reset_password_request(request):
    if request.method == 'POST':
        form = ResetPasswordEmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.get(email=email)

            current_site = get_current_site(request)
            subject = 'Password Reset Request'
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(user.pk.to_bytes())

            reset_link = reverse('account:reset_password_confirm',
                                 kwargs={'uidb64': uid, 'token': token})
            reset_url = f"http://{current_site.domain}{reset_link}"

            message = render_to_string('accounts/password_reset_email.html', {
                'user': user,
                'reset_url': reset_url,
                'domain': current_site.domain,
            })

            send_mail(subject, message, 'noreply@example.com', [email])

            return render(request, 'accounts/reset_password_email_sent.html')
    else:
        form = ResetPasswordEmailForm()

    context = {'form': form}
    return render(request, 'accounts/reset_password_request.html', context)


@login_required
def api_key_display_view(request):
    user = request.user
    api_key = user.api_key
    if api_key:
        return render(request, 'accounts/api_key_display.html',
                      {'api_key': api_key})
    else:
        return render(request, 'accounts/api_key_not_generated.html')


@login_required
def api_key_generation_complete_view(request):
    return render(request, 'accounts/api_key_generation_complete.html')


def api_key_generation_error_view(request):
    return render(request, 'accounts/api_key_generation_error.html')


def api_key_already_generated_view(request):
    return render(request, 'accounts/api_key_already_generated.html')


from django.shortcuts import render


def invalid_activation_link_view(request):
    return render(request, 'accounts/invalid_activation_link.html')


def invalid_reset_link_view(request):
    return render(request, 'accounts/invalid_reset_link.html')


def invalid_email_change_request_link_view(request):
    return render(request, 'accounts/invalid_email_change_request_link.html')


def profile_deleted_view(request):
    return render(request, 'accounts/profile_deleted.html')
