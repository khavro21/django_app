from django.core.mail import send_mail
from email.message import EmailMessage
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

from .forms import ContactForm
from .models import Article, Contact

# Create your views here.
def home(request):
    return render(request, "home.html")


class ArticleListView(ListView):
    model = Article
    template_name = 'articles.html'
    context_object_name = "articles"
    paginate_by = 5

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = "article"

    def get_object(self):
        _id = self.kwargs.get("id")
        _slug = self.kwargs.get("slug")
        return get_object_or_404(Article, id=_id, slug=_slug)




def contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data["name"]
        content = form.cleaned_data["content"]
        email = form.cleaned_data["email"]
        form.save()
        #send e-mail - The actual e-mail is not being send(didn't want to do it with my personal e-mail)
        #send_mail(name, content, email, ["debug@mir.de"], fail_silently=False)
        form = ContactForm() 
        
    context = {'form': form}
    return render(request, 'contact.html', context)

        
