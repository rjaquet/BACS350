from django.urls import path
from pages.views import homePageView, MyView, IndexView, HomeView, AboutView


urlpatterns = [
    path('hulk',IndexView.as_view )),
    path('ironman',HomeView.as_view() ),
    path('blackwidow',AboutView.as_view()),