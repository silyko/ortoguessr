import random
import typing as T
from pathlib import Path
import json

from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
)
from django.urls import reverse
from django.views import generic
from django.conf import settings


from . import models, forms

# Create your views here.
coords = []
with open(Path(__file__).parent / "coords.txt") as f:
    for line in f:
        x, y = line.split()
        coords.append((int(x), int(y)))

print(len(coords), coords[0])


class GameView(LoginRequiredMixin, TemplateView):
    template_name: str = "game/game.html"

    def get_context_data(self, **kwargs: T.Any) -> T.Dict[str, T.Any]:
        context_data = super().get_context_data(**kwargs)
        x, y = random.choice(coords)
        context_data["question_x"] = str(x)
        context_data["question_y"] = str(y)
        context_data["kftoken"] = settings.DATAFORSYNINGEN_TOKEN
        return context_data


class LandingView(LoginRequiredMixin, TemplateView):
    template_name: str = "game/landing.html"

    def get_context_data(self, **kwargs: T.Any) -> T.Dict[str, T.Any]:
        context_data = super().get_context_data(**kwargs)
        qs = list(models.Score.objects.order_by("-score")[:6])
        for n, obj in enumerate(qs):
            obj.rank = n + 1
        context_data["scores"] = qs
        return context_data


def get_question(request, *args, **kwargs):
    obj = {
        "coordinates": random.choice(coords)
    }
    return JsonResponse(obj)


@csrf_exempt
@login_required
def set_score(request, *args, **kwargs):
    if request.method != "POST":
        return HttpResponseBadRequest()
    data = json.loads(request.body.decode("utf-8"))
    models.Score.objects.create(user=request.user, score=data["score"], level=data["level"])
    return JsonResponse("ok", safe=False)


class SignUpView(generic.CreateView):
    form_class = forms.SignupForm
    template_name = "registration/signup.html"

    def get_success_url(self) -> str:
        return reverse("login") + "?next=/"