from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, edit
from .models import ContactModel
from .forms import SubscribeNewsletterForm, ContactForm


class IndexTemplateView(TemplateView):
    template_name = "project/page/index/templates/index.html"

class SubscribeNewsletterFormView(edit.FormView):
    form_class = SubscribeNewsletterForm
    success_url = reverse_lazy('index:home')
    template_name = "project/page/index/templates/includes/footer/boletin.html"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        # Redirige de vuelta a la página actual en caso de error
        return redirect(self.request.META.get('HTTP_REFERER', '/'))
    
class ContactFormView(edit.FormView):
    form_class = ContactForm
    success_url = reverse_lazy('index:home')
    template_name = "project/page/index/templates/includes/sections/contact/form.html"
    
    def form_valid(self, form):
        unique_id = form.cleaned_data.get('unique_id')
        if ContactModel.objects.filter(unique_id=unique_id).exists():
            form.add_error(None, "Este formulario ya ha sido enviado.")
            return self.form_invalid(form)
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        # Redirige de vuelta a la página actual en caso de error
        return redirect(self.request.META.get('HTTP_REFERER', '/'))
