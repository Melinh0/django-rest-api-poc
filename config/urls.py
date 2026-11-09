from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Cinema API",
        default_version="v1",
        description="API for managing movies, theaters, and sessions in a cinema",
        contact=openapi.Contact(email="jonas.nogueira@aluno.uece.br"),
    ),
    public=True,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/movies/", include("movies.urls")),
    path("api/theaters/", include("theaters.urls")),
    path("api/sessions/", include("sessions.urls")),
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
]
