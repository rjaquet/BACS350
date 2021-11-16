from django.urls import path
from django.contrib import admin
from hero.views_hero import IndexView, HeroDeleteView, HeroDetailView, HeroListView, HeroCreateView, HeroUpdateView
from hero.views_chapter import ChapterDeleteView, ChapterDetailView, ChapterListView, ChapterCreateView, ChapterUpdateView
from django.urls.conf import include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',                        IndexView.as_view(),         name='index_view'),
    path('hero/',                   HeroListView.as_view(),      name='hero_list'),
    path('hero/<int:pk>',           HeroDetailView.as_view(),    name='hero_detail'),
    path('hero/add',                HeroCreateView.as_view(),    name='hero_add'),
    path('hero/<int:pk>/',          HeroUpdateView.as_view(),    name='hero_edit'),
    path('hero/<int:pk>/delete',    HeroDeleteView.as_view(),    name='hero_delete'),

    path('chapter/',                ChapterListView.as_view(),   name='chapter_list'),
    path('chapter/<int:pk>',        ChapterDetailView.as_view(),
         name='chapter_detail'),
    path('chapter/add',             ChapterCreateView.as_view(), name='chapter_add'),
    path('chapter/<int:pk>/',       ChapterUpdateView.as_view(), name='chapter_edit'),
    path('chapter/<int:pk>/delete',
         ChapterDeleteView.as_view(), name='chapter_delete'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', RedirectView.as_view(url='accounts/'), name='home'),

    # Document
    path('', include('doc.urls')),
]
