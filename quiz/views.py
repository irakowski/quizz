from django.shortcuts import render
from rest_framework import generics
from .serializers import CategorySerializer, QuestionSerializer
from . import models

# Create your views here.
class CategoryView(generics.ListAPIView):
    """
    Returns All categories with questions 
    """
    serializer_class = CategorySerializer
    queryset = models.Category.objects.all()


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Returns all questions in specific category
    """
    queryset = models.Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'

class QuestionView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializer
    queryset = models.Question.objects.all()