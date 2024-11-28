from django.urls import path
from .views import LisBooksView

urlpatterns = [path("", LisBooksView.as_view(), name="home")]
