from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class SessionsPageView(TemplateView):
    template_name = 'sessions.html'

class ProtocolPage(TemplateView):
    template_name = 'sessionsProtocol.html'
