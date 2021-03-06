from django.http import HttpResponse
from django.template import loader
import logging

logger = logging.getLogger(__name__)


def index(request):
    template = loader.get_template('actions.html')
    context = {
        'title': 'Home'
    }
    return HttpResponse(template.render(context, request))
