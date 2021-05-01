from django.db import models
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name

    
    def save(self, *args, **kwargs):
        """
        Automatically creates slug for category name
        """
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)    


class Question(models.Model):
    text = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return self.text