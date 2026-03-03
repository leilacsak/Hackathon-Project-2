from django.db import models


class Booking(models.Model):
    class Surface(models.TextChoices):
        HARD = "hard", "Hard"
        CLAY = "clay", "Clay"
        GRASS = "grass", "Grass"

    player_name = models.CharField(max_length=100)
    player_email = models.EmailField()
    date = models.DateField()
    start_time = models.TimeField()
    duration_minutes = models.PositiveIntegerField(default=60)
    court_number = models.PositiveSmallIntegerField(default=1)
    surface = models.CharField(
        max_length=10,
        choices=Surface.choices,
        default=Surface.HARD,
    )
    notes = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["date", "start_time"]

    def __str__(self):
        return f"Court {self.court_number} - {self.player_name} ({self.date})"
