from rest_framework import serializers

from questions.models import Questions


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "Question V2"
        model = Questions
        fields = "__all__"
