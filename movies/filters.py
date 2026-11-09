from rest_framework import filters


class MovieFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        title = request.query_params.get("name")
        if title:
            queryset = queryset.filter(name__icontains=title)
        return queryset
