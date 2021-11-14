from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .views import (
    BooksListView, Search, register, LoginUser, logout_user, selectdate, profile
)


urlpatterns = [
    path('', BooksListView.as_view(), name='mainpage'),
    path('search', Search.as_view(), name='search'),
    path('register/', register, name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('selectdate/<booka>', selectdate, name='selectdate'),
    path('profile/<username>', profile, name='profile'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)