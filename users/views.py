from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# Create your views here.
def register(request):
    """REgister a new user."""
    if request.method != 'POST':
        # Отображаем бланк формы регистрации.
        form = UserCreationForm()
    else:
        # Процесс завершения формы.
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_users = form.save()
            # Добавление пользователя и перенаправление на домашнюю страницу.
            login(request, new_users)
            return redirect('learning_logs:index')

    # Отображение бланка недопустимой формы.
    context = {'form': form}
    return render(request, 'registration/register.html', context)