from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from django.template import loader
from django.shortcuts import redirect
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
            return redirect('/blog')

    form = CreatePostForm()
    return render(request, 'blog/create.html', {'form': form})


def addAuthor(request):
    if request.method == 'POST':
        form = CreateAuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/blog/create')

    form = CreateAuthorForm()
    return render(request, 'blog/addAuthor.html', {'form': form})


def edit(request, pk):

    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            post.title = form.data['title']
            post.author.id = get_object_or_404(Author, pk=form.data['author'])
            post.description = form.data['description']
            post.created_date = form.data['created_date']
            post.save()
            return redirect('/blog/' + str(pk))

    authors = Author.objects.order_by('name')[:]
    context = {
        'post': post,
        'authors': authors,
    }
    return render(request, 'blog/edit.html', context)
