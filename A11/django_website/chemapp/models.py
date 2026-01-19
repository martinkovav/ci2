from django.db import models

# Create your models here.
class Smiles(models.Model):
    smiles_text = models.CharField(max_length=200)
    date_time_received = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.smiles_text