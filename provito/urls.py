from django.urls import path
from .views import index, BoardList


urlpatterns = [
    # path('', index)
    path('', BoardList.as_view()),
]
