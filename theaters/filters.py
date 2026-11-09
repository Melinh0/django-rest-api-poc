from rest_framework import filters


class TheaterFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        number = request.query_params.get("number")
        if number:
            queryset = queryset.filter(number__icontains=number)
        return queryset
