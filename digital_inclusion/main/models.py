from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class UIComponent(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    text = RichTextField()
    def __str__(self):
        return self.name