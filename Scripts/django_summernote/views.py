import logging
from django import VERSION as django_version
from django.contrib.auth.mixins import UserPassesTestMixin
from django.templatetags.static import static
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
if django_version >= (3, 0):
    from django.utils.translation import gettext as _
else:
    from django.utils.translation import ugettext as _
from django.views.generic import TemplateView

from .utils import using_config, has_codemirror_config

logger = logging.getLogger(__name__)

try:
    # Django >= 1.10
    from django.views import View
except ImportError:
    from django.views.generic import View


class SummernoteEditor(TemplateView):
    template_name = 'django_summernote/widget_iframe_editor.html'

    @using_config
    def __init__(self):
        super(SummernoteEditor, self).__init__()

        static_default_css = tuple(static(x) for x in config['default_css'])
        static_default_js = tuple(static(x) for x in config['default_js'])
        self.css = \
            config['base_css'] \
            + (config['codemirror_css'] if has_codemirror_config() else ()) \
            + static_default_css \
            + config['css']

        self.js = \
            config['base_js'] \
            + (config['codemirror_js'] if has_codemirror_config() else ()) \
            + static_default_js \
            + config['js']

    @using_config
    def get_context_data(self, **kwargs):
        context = super(SummernoteEditor, self).get_context_data(**kwargs)

        context['id'] = self.kwargs['id']
        context['id_safe'] = self.kwargs['id'].replace('-', '_')
        context['css'] = self.css
        context['js'] = self.js
        context['config'] = config

        return context


