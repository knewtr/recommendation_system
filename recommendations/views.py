from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from config.settings import CACHE_ENABLED
from recommendations.algorithms.knn import KNNeighbour
from recommendations.algorithms.pagerank import PageRank


class RecommendationView(TemplateView):
    template_name = "recommendations.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.request.user.id
        if not CACHE_ENABLED:
            recs = {
                "pr_rec": PageRank.recommendations(user_id, 5),
                "knn_rec": KNNeighbour.recommendations(user_id, 5),
            }
        else:
            key = "recs"
            recs = cache.get(key)
            if not recs:
                recs = {
                    "pr_rec": PageRank.recommendations(user_id, 5),
                    "knn_rec": KNNeighbour.recommendations(user_id, 5),
                }
                cache.set("recs", recs, timeout=300)
        context.update(recs)
        return context
