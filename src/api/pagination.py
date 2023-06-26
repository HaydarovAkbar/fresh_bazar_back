# Pagination for News
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class DefaultPagination(PageNumberPagination):
    page_size = 20

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'per_page': self.page_size,
            'current_page': self.page.number,
            'total_pages': self.page.paginator.num_pages,
            # 'page_items': len(self.page),
            'total': self.page.paginator.count,
            'results': data
        })


class Short(DefaultPagination):
    page_size = 4


class DoubleShort(DefaultPagination):
    page_size = 8


class MidShort(DefaultPagination):
    page_size = 9


class ExtraShort(DefaultPagination):
    page_size = 10


class Middle(DefaultPagination):
    page_size = 12


class ExtraMiddle(DefaultPagination):
    page_size = 15