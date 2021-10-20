from django.views.generic import TemplateView


class HulkView(TemplateView):
    template_name = 'hulk.html'
    
    def get_context_data(self, **kwargs):
        return {
            'title': 'About this Class', 
            'body': 'Once upon a time ...',
        }
 
class IronMan(TemplateView):
    template_name = "iron_man.html"
    
    def get_context_data(self, **kwargs):
        return {
            'title': 'My Home Page', 
            'body': 'This page is boring ...',
        }
 

class BlackWidow(TemplateView):
    template_name = "black_widow.html"
