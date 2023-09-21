from django.urls import path
from .views import HomePageView, AboutPageView, ProcuctsPageView

urlpatterns = [
    path("about/", AboutPageView.as_view(), name = "about"),
    path("", HomePageView.as_view(), name = "home"),
    path("products/",ProcuctsPageView.as_view(), name = "products")
]