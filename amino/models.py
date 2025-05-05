from django.db import models

class AminoAcid(models.Model):
    name = models.CharField(max_length=50, unique=True)
    three_letter_code = models.CharField(max_length=3)
    one_letter_code = models.CharField(max_length=1)
    structure_image = models.ImageField(upload_to='structures/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
