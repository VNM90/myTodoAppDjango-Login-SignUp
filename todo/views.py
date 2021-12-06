from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Todo
from .forms import TodoForm, SignUpForm
from myTodoApp.settings import LOGIN_URL


@login_required(login_url=LOGIN_URL)
def home(request):
    todo = Todo.objects.filter(user=request.user)
    return render(request, 'home.html', {'todo': todo})


@login_required(login_url=LOGIN_URL)
def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        user = get_user(request)
        form = TodoForm(initial={'user': user})

    return render(request, 'create.html', {'form': form})


@login_required(login_url=LOGIN_URL)
def delete(request, id):
    delete_element = get_object_or_404(Todo, pk=id)
    delete_element.delete()
    return redirect('home')


@login_required(login_url=LOGIN_URL)
def update(request, id):
    obj = get_object_or_404(Todo, pk=id, user=request.user)
    form = TodoForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'create.html', {'form': form})


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        # form = UserCreationForm()
        form = SignUpForm()
        if request.method == 'POST':
            # form = UserCreationForm(request.POST)
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'New user added')
                return redirect('home')
            else:
                messages.info(request, 'Username or password is incorrect')
        return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or password is incorrect')

        return render(request, 'login.html')


@login_required(login_url=LOGIN_URL)
def logout_view(request):
    logout(request)
    return redirect('home')
