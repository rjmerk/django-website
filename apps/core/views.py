from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from .models import Article


class Index(TemplateView):
    template_name = "index.html"


class ArticleDetail(LoginRequiredMixin, DetailView):
    model = Article
