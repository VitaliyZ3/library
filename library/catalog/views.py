from django.db import models
from django.shortcuts import render
from django.views.generic import ListView
from .models import Book
# Create your views here.

class BooksListView(ListView):

    model = Book
    fields = '__all__'