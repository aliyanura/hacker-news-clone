from .models import Story


def drop_score():
    """Daily drop score"""

    scores = [s for s in Story.objects.all()]
    for s in scores:
        s.score = 0
        s.save()
