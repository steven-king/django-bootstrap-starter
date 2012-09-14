#-*- encoding: utf-8 -*-

from django.forms.models import ModelForm
from testapp.models import Person
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Layout, Submit, Button, HTML
from crispy_forms.bootstrap import FormActions
from django.core.urlresolvers import reverse


class PersonForm(ModelForm):
    
    helper = FormHelper()
    helper.form_tag = False
    helper.layout = Layout(
            'name',
            'email',
#            FormActions(
#            HTML('<button type="submit" class="btn btn-primary">Save</button>'),
#            HTML('<button href="/" class="btn">Cancel</button>'),
#            )
    )
    
    class Meta:
        model = Person