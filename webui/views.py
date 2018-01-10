from django.shortcuts import render,redirect
from vanilla import TemplateView
class IndexViews(TemplateView):
    template_name = 'webui/index.html'
    def get_context_data(self, **kwargs):
        context = super(IndexViews, self).get_context_data(**kwargs)
        context['title'] = u'删除'
        context['delete_confirmation'] = u'确实删除么'
        context['btnsubmit'] = u'提交'
        context['btncancel'] = u'取消'
        context['username'] = self.request.user.last_name
        context['is_superuser'] = self.request.user.is_superuser
        context['active'] = "index"
        return context