from django.urls import path
from pages.views import homePageView, MyView, IndexView, HomeView, AboutView


urlpatterns = [
    path('',IndexView.as_view )),
    path('home',HomeView.as_view() ),
    path('about',AboutView.as_view()),
]
