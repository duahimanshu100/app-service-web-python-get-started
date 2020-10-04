from rest_framework import viewsets

from questions.api.v1.serializers import QuestionSerializer
from questions.models import Questions

from rest_framework import generics, permissions, serializers

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope


class QuestionViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing question instances.
    """

    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    serializer_class = QuestionSerializer
    queryset = Questions.objects.all()
