# django.views.generic.base.TemplateView Renders a given template,
# with the context containing parameters captured in the URL.
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView): # new
    template_name = 'about.html'

