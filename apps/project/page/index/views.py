from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, edit
from .models import ContactModel
from .forms import SubscribeNewsletterForm, ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse


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

        contact = form.save()

        send_mail(
            subject='Fundación Leirion | Hemos recibido tu mensaje',
            message=(
                f'Gracias {contact.names} por contactarnos.\n'
                f'Hemos recibido su mensaje y nos pondremos en contacto con usted pronto.'
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[contact.email],
            fail_silently=False
        )

        admin_link = reverse(
            'admin:index_contactmodel_change', args=[contact.id])
        admin_url = self.request.build_absolute_uri(admin_link)
        send_mail(
            subject=f'Nuevo mensaje | CONTACTO | {contact.title}',
            message=(
                f'Se ha recibido un nuevo mensaje,\n'
                f'Puede verlo en el siguiente enlace: {admin_url}\n\n'
                f'INFORMACIÓN:\n'
                f'Nombres: {contact.names}\n'
                f'Titulo: {contact.title}\n'
                f'Mensaje: \n{contact.message}\n'
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['info@fundacionleirion.com'],
            fail_silently=False
        )

        return super().form_valid(form)

    def form_invalid(self, form):
        # Redirige de vuelta a la página actual en caso de error
        return redirect(self.request.META.get('HTTP_REFERER', '/'))
