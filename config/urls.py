from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("lms.urls")),
    path("users/", include("users.urls", namespace="users")),
]
