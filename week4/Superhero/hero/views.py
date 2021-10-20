from django.views.generic import TemplateView


class IndexView(TemplateView:)
    template_name = 'index.html'


class HulkView(TemplateView):
    template_name = 'hero.html'
    
    def get_context_data(self, **kwargs):
        return {
            'title': "Hulk", 
            'body': 'My name is Bruce Banner...',
            'image': '/static/images/hulk.jpg'
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
