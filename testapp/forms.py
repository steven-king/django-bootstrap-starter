#-*- encoding: utf-8 -*-

from django.forms.models import ModelForm
from testapp.models import Person
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Layout, Submit, Button, HTML, Field
from crispy_forms.bootstrap import FormActions, PrependedText, AppendedText
from django.core.urlresolvers import reverse

# Custom django-crispy-forms bootstrap field
class DateBootstrap(AppendedText):
    def __init__(self, field):
        super(DateBootstrap, self).__init__(field, '<i class="icon-th"></i>', template='date-crispy.html')

class PersonForm(ModelForm):
    
    helper = FormHelper()
    helper.form_tag = False
    helper.layout = Layout(
            'name',
            DateBootstrap('date_of_birth'),
            PrependedText('email', '<i class="icon-envelope"></i>'),
    )
    
    class Meta:
        model = Person