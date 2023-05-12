# <-- Importing Files -->
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm,SetPasswordForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .forms import EmployeeLoginForm
from django.contrib.auth import get_user_model

# <-- Login Function -->
def login_view(request):
    if request.method == 'POST':
        form = EmployeeLoginForm(request.POST)
        if form.is_valid():
            employee_id = form.cleaned_data['employee_id']
            password = form.cleaned_data['password']
            user = authenticate(request, username=employee_id, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Invalid employee ID or password.")
    else:
        form = EmployeeLoginForm()
    return render(request, 'staff/login.html', {'form': form})

# <-- Home Function -->
@login_required
def home(request):
        return render(request, 'staff/home.html')

# <-- Logout Function --> 
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

# <-- Creating USER -->
User = get_user_model()

def create_user(username, password):
    user = User.objects.create_user(
        username=username,
        password=password,
    )
    return user

# <-- Password Reseting Function -->
    # <-- password Reset page -->
class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset.html'
    email_template_name = 'registration/password_reset_email.html'
    form_class = PasswordResetForm
    success_url = reverse_lazy('password_reset_done')

    # <--  Emailing the password rese form -->
class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'

    # <-- Confirming the password Reseting --> 
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    form_class = SetPasswordForm
    success_url = reverse_lazy('password_reset_complete')

    # <-- Password Reset Completed -->
class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'

