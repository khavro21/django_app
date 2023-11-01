from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("articles/", views.ArticleListView.as_view(), name="articles"),
    path("articles/<int:id>/<slug:slug>/", views.ArticleDetailView.as_view(), name="article-detail"),
    path("contact", views.contact, name="contact")
]   
