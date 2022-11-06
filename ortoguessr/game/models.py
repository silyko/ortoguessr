from calendar import c
from django.db import models
from django.db.models import Max

# Create your models here.

class Score(models.Model):
    score = models.PositiveIntegerField()
    level = models.PositiveSmallIntegerField(null=True)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    @classmethod
    def high_score(cls) -> "Score":
        qs = cls.objects.aggregate(high_score=Max("score"))
        if not qs["high_score"]:
            return None
        return cls.objects.filter(score=qs["high_score"]).first()

