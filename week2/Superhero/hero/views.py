from django.views.generic import TemplateView


class DeadpoolView(TemplateView):
    template_name = 'deadpool.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'My About Page',
            'body': 'Once upon a time ...',
        }


class BatmanView(TemplateView):
    template_name = "batman.html"


class HarleyQuinn(TemplateView):
    template_name = 'harley_quinn.html'
