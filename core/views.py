from django.db.models import Q
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .models import ContactMessage
from .models import Post
from django.views.generic import TemplateView, ListView, DetailView
from .forms import *


class HomeView(ListView):
    model = Post
    template_name = 'core/home.html'  # Your template name
    context_object_name = 'posts'  # Variable name in the template
    paginate_by = 15  # Show 15 posts per page

    def get_queryset(self):
        query = self.request.GET.get('q')
        # Default queryset - all posts ordered by created_at
        queryset = Post.objects.all().order_by('-created_at')

        # Apply search filter if query is present
        if query:
            queryset = queryset.filter(Q(title__icontains=query) | Q(content__icontains=query))

        return queryset

class AboutView(TemplateView):
    template_name = 'core/about.html'

class ProjectsView(TemplateView):
    template_name = 'core/projects.html'

class ContactView(FormView):
    template_name = 'core/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('core:thank-you')  # Redirect to thank-you page

    def form_valid(self, form):
        # Save contact message to database
        contact_message = ContactMessage(
            name=form.cleaned_data['name'],
            email=form.cleaned_data['email'],
            phone=form.cleaned_data['phone'],
            message=form.cleaned_data['message']
        )
        contact_message.save()


        return super().form_valid(form)

class ThankYouView(TemplateView):
    template_name = 'core/thank_you.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'core/post_detail.html'  # Your template for individual post details
    context_object_name = 'post'  # Variable name used in the template

