from apps.project.page.index.forms import SubscribeNewsletterForm

def custom_processors(request):
    ctx = {}
    ctx['subscribe_form'] = SubscribeNewsletterForm()
    return ctx