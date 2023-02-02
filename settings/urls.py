from django.contrib import admin
from django.urls import path

from apps.main.views import PenView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pen_create/',PenView.as_view()),
]
