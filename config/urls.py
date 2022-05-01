from src.books.api import router as books_router
from src.core.api import router as core_router

from ninja import NinjaAPI

from django.contrib import admin
from django.urls import path

api = NinjaAPI()


api.add_router("", core_router)
api.add_router("/books/", books_router)


urlpatterns = [path("admin/", admin.site.urls), path("api/", api.urls)]
