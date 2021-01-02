from django.db import models

# Create your models here.

class GetQuate(models.Model):
    zip_code = models.IntegerField(null=False)
    select_type = models.CharField(max_length=260,null=False)

    def __str__(self):
        return self.select_type

