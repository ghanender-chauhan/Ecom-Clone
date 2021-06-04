from django.urls import path
from .import views

urlpatterns = [
    path("", views.index , name = "amazon"),
    path("about/", views.about , name = "about"),
    path("contact/", views.contact , name = "contact"),
    path("productview/", views.productview , name = "productview"),
    path("tracker/", views.tracker , name = "tracker"),
    path("checkout/", views.checkout  , name = "checkout"),
    path("search/", views.search , name = "search"),
]
