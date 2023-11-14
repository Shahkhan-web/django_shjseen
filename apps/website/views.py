from django.utils.translation import gettext_lazy as _
from django.http import HttpResponse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from apps.participant.models import Category, Participant
from apps.website import forms


class LandingPageView(generic.TemplateView):
    template_name = 'landing_page.html'

class aboutUs(generic.TemplateView):
    template_name = 'aboutUs.html'

class contact(generic.TemplateView):
    template_name = 'contactus.html'

class media(generic.TemplateView):
    template_name = 'media.html'
class award(generic.TemplateView):
    template_name = 'award.html'
class terms(generic.TemplateView):
    template_name = 'terms.html'

class ParticipatePageView(generic.FormView):
    template_name = 'participate_page.html'
    form_class = forms.ParticipateForm

    def get_context_data(self, **kwargs):
        context = super(ParticipatePageView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.values(
            'id',
            'name'
        ).unarchived()
        context['organization_locations'] = [
            {
                'name': y,
                'value': x
            } for x, y in Participant.ORGANIZATION_LOCATION_CHOICES
        ]
        return context


class ParticipateConfirmationPageView(generic.TemplateView):
    template_name = 'participate_confirmation_page.html'


@csrf_exempt
def register_participant(request):
    if request.method == 'POST':
        form = forms.ParticipateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse({'detail': _('Registered Successfully.')})
        else:
            print(form.errors)
            return HttpResponse({'detail': _('Failed')}, status=400)

