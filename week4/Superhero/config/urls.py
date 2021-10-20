from django.urls import path
from hero.views import HulkView, BlackWidow, IronMan


urlpatterns = [
    path('hulk', HulkView.as_view()),
    path('ironman',IronMan.as_view() ),
    path('blackwidow',BlackWidow.as_view()),
]