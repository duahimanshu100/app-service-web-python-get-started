import rest_framework.mixins
from rest_framework.response import Response


class CisCreateModelMixin(rest_framework.mixins.CreateModelMixin):
    """
    Create a model instance.
    """
    def create(self, request, *args, **kwargs):
        response: Response = super(CisCreateModelMixin, self).create(request, *args, **kwargs)
        data = response.data
        response_dict: dict = {
            "success": True,
            "error": "",
            'data': data,
            "statusCode": 100
        }
        response.data = response_dict

        return response


class CisListModelMixin(rest_framework.mixins.ListModelMixin):
    """
    List a queryset.
    """
    def list(self, request, *args, **kwargs):
        response: Response = super(CisListModelMixin, self).list(request, *args, **kwargs)
        data = response.data
        response_dict: dict = {
            "success": True,
            "error": "",
            'data': data,
            "statusCode": 100
        }
        response.data = response_dict

        return response


class CisRetrieveModelMixin(rest_framework.mixins.RetrieveModelMixin):
    """
    Retrieve a model instance.
    """
    def retrieve(self, request, *args, **kwargs):
        response: Response = super(CisRetrieveModelMixin, self).retrieve(request, *args, **kwargs)
        data = response.data
        response_dict: dict = {
            "success": True,
            "error": "",
            'data': data,
            "statusCode": 100
        }
        response.data = response_dict

        return response


class CisUpdateModelMixin(rest_framework.mixins.UpdateModelMixin):
    """
    Update a model instance.
    """
    def update(self, request, *args, **kwargs):
        response: Response = super(CisUpdateModelMixin, self).update(request, *args, **kwargs)
        data = response.data
        response_dict: dict = {
            "success": True,
            "error": "",
            'data': data,
            "statusCode": 100
        }
        response.data = response_dict

        return response