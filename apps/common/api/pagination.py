from rest_framework.pagination import PageNumberPagination
from apps.common.api.responses import success_response

class DefaultPagination(PageNumberPagination):
    """
    Default pagination for all APIs.
    """

    page_size = 10

    page_size_query_param = "page_size"

    max_page_size = 100
    
    page_query_param = "page"
    
    def get_paginated_response(self, data):

        return success_response(
                data={
                    "count": self.page.paginator.count,
                    "next": self.get_next_link(),
                    "previous": self.get_previous_link(),
                    "results": data,
                },
        )