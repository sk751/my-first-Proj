from django.shortcuts import render
from django.views.generic import TemplateView


class classA(TemplateView):
	def get(self, request, **kwargs):
	   return render(request, 'HTMLToPrint.html', context=None)
	   
	   
class classB(TemplateView):
	template_name = "HTMLLinkA.html"
	
class classC(TemplateView):
	def get(self, request, **kwargs):
	   return render(request, 'tryB.html', context=None)	