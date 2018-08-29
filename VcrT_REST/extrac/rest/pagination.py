from rest_framework.pagination import LimitOffsetPagination, CursorPagination

class VcrTLOPager(LimitOffsetPagination):
    """
        自定义 - Limit 分页
    """
    default_limit = 12
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 60

class VcrTCPPager(CursorPagination):
    """
        自定义 - Cursor 分页
    """
    page_size = 20
    cursor_query_param = 'cursor'
    ordering = '-id'
    page_size_query_param = 'size'
    max_page_size = 5