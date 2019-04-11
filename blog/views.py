from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse
from .models import Post
from .models import Author
from .forms import CreatePostForm, CreateAuthorForm


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        """Return the last five published questions."""
        return Post.objects.order_by('created_date')[:]


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'


class ResultsView(generic.DetailView):
    model = Post
    template_name = 'blog/results.html'


def create(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            form.save()

    form = CreatePostForm()
    return render(request, 'blog/create.html', {'form': form})


def edit(request, question_id):
    post = Post.objects.order_by('created_date')[question_id-1]
    template = loader.get_template('blog/edit.html')
    context = {
        'post': post,
    }
    return HttpResponse(template.render(context, request))
