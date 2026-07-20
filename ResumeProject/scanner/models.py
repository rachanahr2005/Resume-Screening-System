from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=255)
    skills = models.TextField()
    score = models.FloatField()
    prediction = models.CharField(max_length=50,default="Unknown")
    probability = models.FloatField(default=0.0)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-score']