from django.urls import reverse_lazy
from django.views.generic import edit

from .forms import SubscribeNewsletterForm


class IndexTemplateView(edit.FormView):
    template_name = "project/page/index/templates/index.html"
    form_class = SubscribeNewsletterForm
    success_url = reverse_lazy('index:home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
