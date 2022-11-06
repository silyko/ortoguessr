"""ortoguessr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from game.views import GameView, LandingView, get_question, set_score, SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('game/<int:level>/', GameView.as_view()),
    path("accounts/", include("django.contrib.auth.urls")),  # new
    path('accounts/signup/', SignUpView.as_view()),
    path('', LandingView.as_view()),
    path('api/q/', get_question),
    path('api/score/', set_score),
]
