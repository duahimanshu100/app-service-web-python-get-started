from rest_framework import viewsets

from cis.api_mixins import CisListModelMixin, CisRetrieveModelMixin, CisCreateModelMixin,CisUpdateModelMixin


class CisModelViewSet(viewsets.ModelViewSet,CisListModelMixin,
                      CisRetrieveModelMixin,CisCreateModelMixin,
                      CisUpdateModelMixin):
    def get_object(self):
        """
        Returns the object the view is displaying.

        You may want to override this if you need to provide non-standard
        queryset lookups.  Eg if objects are referenced using multiple
        keyword arguments in the url conf.
        """
        self.kwargs[self.lookup_field] = self.request.data.get(self.lookup_field) or self.kwargs.get(self.lookup_field)
        return super(CisModelViewSet, self).get_object()
