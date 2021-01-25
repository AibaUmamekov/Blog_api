from rest_framework.pagination import (
    LimitOffsetPagination,
)


class PostLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 3
    max_limit = 6
