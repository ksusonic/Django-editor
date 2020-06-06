from django.conf.urls import url

from .views import SummernoteEditor


urlpatterns = [
    url(r'^editor/(?P<id>.+)/$', SummernoteEditor.as_view(),
        name='django_summernote-editor'),
]
