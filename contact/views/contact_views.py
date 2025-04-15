from django.shortcuts import get_object_or_404, render # type:ignore
from contact.models import Contact

def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')[0:10]
    context = {
        'contacts': contacts,
        'site_title': 'Contatos'
    }

    return render(
        request,
        'contact/index.html',
        context

)

def contact(request, contact_id):
    singleContact = get_object_or_404(Contact, pk=contact_id, show=True)
    context = {
        'contact': singleContact,
        'site_title': singleContact.first_name
    }

    return render(
        request,
        'contact/contact.html',
        context
)