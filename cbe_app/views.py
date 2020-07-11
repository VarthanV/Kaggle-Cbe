from django.shortcuts import render
from django.views.generic import View

class HomeView(View):
    template_name = 'cbe_app/index.html'
    def get(self,request):
        return render(request,self.template_name)