from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "fate/index.html"  # 指定模板路径
    
    # 如需传递数据到模板
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tech_stack'] = [
            {'name': 'Django', 'icon': 'fa-server'},
            {'name': 'Vue', 'icon': 'fa-vuejs'},
            {'name': 'MySQL', 'icon': 'fa-database'}
        ]
        return context