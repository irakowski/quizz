from . import models
from rest_framework import serializers

class AnswerSerializer(serializers.ModelSerializer):
	class Meta:
		fields = [
			'id',
			'text',
			'is_correct',
		]
		model = models.Answer


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(read_only=True, many=True)

    class Meta: 
        fields = [
            'id', 
            'text', 
            'answers']
        model = models.Question

class CategorySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(read_only=True, many=True)
    count = serializers.SerializerMethodField()
    lookup_field = 'slug'

    def get_count(self, obj):
       count = obj.questions.count()
       return count
    
    class Meta:
        model = models.Category
        fields = [
            'id', 
            'name',
            'count',
            'slug',
            'questions'
            ]
            



