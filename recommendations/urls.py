from django.urls import path

from recommendations.apps import RecommendationsConfig
from recommendations.views import RecommendationView

app_name = RecommendationsConfig.name

urlpatterns = [
    path("recommendations/", RecommendationView.as_view(), name="recommendations"),
]
