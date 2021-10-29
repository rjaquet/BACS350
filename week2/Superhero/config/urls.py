from django.urls import path
from hero.views import HulkView, BlackWidow, IronManView
from week2.Superhero.hero.views import BatmanView, DeadpoolView, HarleyQuinn

urlpatterns = [
    path('harley_quinn', HarleyQuinn.as_view()),
    path('batman', BatmanView.as_view()),
    path('deadpool', DeadpoolView.as_view()),
]
