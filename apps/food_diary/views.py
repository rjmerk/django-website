from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = "food_diary/index.html"
