from apps.project.page.index.forms import SubscribeNewsletterForm, ContactForm

def custom_processors(request):
    ctx = {}
    ctx['subscribe_form'] = SubscribeNewsletterForm()
    ctx['contact_form'] = ContactForm()
    return ctx