from django.db import models
from django.shortcuts import render
from django.views.generic import ListView
from .models import Book, Ticket
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import UserRegistrationForm, UserLoginForm, SelectBookForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.models import User

# Create your views here.

class BooksListView(ListView):
    paginate_by = 5
    model = Book
    fields = '__all__'

def profile(request, username):
    user = User.objects.get(username=username)
    tickets = Ticket.objects.filter( reader = user)
    print(tickets)
    context = {
       "user": user, 
       "tickets" : tickets
    }
    return render(request, 'catalog/profile.html', context)

class Search(ListView):

    def get_queryset(self):
        return Book.objects.filter( name__icontains = self.request.GET.get('q'))
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['q'] = self.request.GET.get('q')
        return context 

class LoginUser(LoginView):
    form_class = UserLoginForm
    template_name = 'catalog/login.html'

def logout_user(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('mainpage')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'catalog/register.html', {'user_form': user_form})

def selectdate(request, booka):
    form = SelectBookForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.reader = request.user
            new_post.book = Book.objects.get(pk = booka)
            new_post.save()
            return redirect('mainpage')
    return render(request, 'catalog/selectdate.html', {'form' : form})

