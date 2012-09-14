# Create your views here.
from django.template.loader import render_to_string
from django import http
from django.utils import simplejson as json
from django.template.context import RequestContext
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from testapp.models import Person
from testapp.forms import PersonForm

# Mixin for Ajax calls
class JSONResponseMixin(object):
    """
    Mixin que renderiza a string un template y lo responde como json 
    """
    
    def render_to_response(self, context):
        content = render_to_string(self.template_name, context, context_instance=RequestContext(self.request))
        
        return http.HttpResponse(json.dumps({'content' : content}), 
                                 content_type='application/json' )
        
##########
# Examples
##########

class PersonCreate(CreateView):
    
    form_class = PersonForm
    template_name = "person_create.html"
    success_url = '/'
    

class PersonList(ListView):
    
    model = Person
    template_name = "person_list.html"
    
    