from django.views.generic import TemplateView

class IndexTemplateView(TemplateView):
    template_name = "project/page/index/templates/index.html"