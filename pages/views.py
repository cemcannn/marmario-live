from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from products.models import Product
from django.views.generic.edit import FormView
from . forms import ContactForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

# def index(request):
#     return render(request, 'index.html')

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all().order_by('-date')[:3]
        context['total_product'] = Product.objects.all().count()
        return context

# def about(request):
#     return render(request, 'about.html')

class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(SuccessMessageMixin ,FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    success_message = 'We received your request'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
