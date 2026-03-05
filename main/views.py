from django.shortcuts import render
from .forms import NameForm
from .models import UserName


def index(request):
    greeting_message = None
    form = NameForm()

    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            # Сохраняем имя в базу данных
            user_name = form.save()
            greeting_message = f"Привет, {user_name.name}! Добро пожаловать на страничку."
            form = NameForm() # очищаем форму
        else:
            # Обработка ошибки пустого поля
            greeting_message = "Пожалуйста, введите ваше имя."

    # Получаем последние 5 сохраненных имен для отображения
    recent_names = UserName.objects.order_by('-id')[:10]

    context = {
        'form': form,
        'greeting_message': greeting_message,
        'recent_names': recent_names,
    }
    return render(request, 'main/index.html', context)