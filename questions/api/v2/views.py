import logging

logger = logging.getLogger(__name__)

from rest_framework import viewsets, filters, permissions

from questions.models import Questions

from questions.api.v2.serializers import QuestionSerializer
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope


class QuestionViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing question instances.
    """

    serializer_class = QuestionSerializer
    queryset = Questions.objects.all()

    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ["description", "id"]
    search_fields = [
        "description",
    ]

    def list(self, request, *args, **kwargs):
        logger.info("Before the Question V2 List ")
        result = super(QuestionViewSet, self).list(request, *args, **kwargs)
        logger.info("After the Question V2 List ")
        return result
