from django.shortcuts import render
from .models import VlogPost
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy


# Create your views here.

class Parent_list_view(ListView):
    #parent class for listviews
    model = None #specified in children
    template = None # --""--
    context_object_name = 'object'
    pagination = 10 #default value

    def filtering(self):
        return self.get_queryset()
    
class Parent_detail_view(DetailView):
    model = None
    template = None
    context_object_name = 'object'



class Parent_create_view(CreateView):
    model = None
    template_name = None
    fields = []

class Parent_update_view(UpdateView):
    model = None
    template = None
    fields = []
        


class VlogPostListView(Parent_list_view):
    """Child class for listing VlogPosts with specific filtering."""
    
    model = VlogPost  # Set the model for this ListView
    template_name = "vlogpost/vlogpost_list.html"  # Specify the template to use
    context_object_name = "vlogposts"  # Name for accessing objects in the template
    paginate_by = 10  # Override the default pagination if needed

    def filtering(self):
        """
        Implement filtering for the child class.
        Filters based on query parameters like title, author, tags, or published_date.
        """
        queryset = super().filtering()
        
        # Dynamic filters from query parameters
        title = self.request.GET.get("title")
        author = self.request.GET.get("author")
        tags = self.request.GET.get("tags")
        published_date = self.request.GET.get("published_date")

        if title:
            queryset = queryset.filter(title__icontains=title)
        if author:
            queryset = queryset.filter(author__icontains=author)
        if tags:
            # Split and filter tags if provided
            tag_list = [tag.strip() for tag in tags.split(",") if tag.strip()]
            queryset = queryset.filter(tags__icontains=",".join(tag_list))
        if published_date:
            queryset = queryset.filter(published_date=published_date)
        
        return queryset

class VlogPostDetailView(Parent_detail_view):
    model = VlogPost  # Set the model for this DetailView
    template_name = "vlogpost/vlog_detail.html"  # Specify the template to use
    context_object_name = "vlogpost"  # Name for accessing objects in the template
""" example url pattern -- come back to this not finished


/vlogs/5/


     """


class VlogPostCreateView(Parent_create_view):
    model = VlogPost  # Specify the model
    template_name = "vlogpost/vlogpost_form.html"  # Template for the create form
    fields = ['title', 'video_url', 'description', 'author', 'published_date', 'tags']  # Fields to include in the form
    success_url = reverse_lazy('vlogpost_list')  # Redirect to the list view after creation



class VlogPostUpdateView(Parent_update_view):
    model = VlogPost
    template_name = "vlogpost/vlogpost_form.html"
    fields = ['title', 'video_url', 'description', 'author', 'published_date', 'tags']
    success_url = reverse_lazy('vlogpost_list')  # Redirect to vlog list after update
