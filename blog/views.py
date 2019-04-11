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


# def index(request):
# return HttpResponse("Hello, world. You're at the polls index.")


# def index(request):
#     posts = Post.objects.order_by('created_date')[:5]
#     template = loader.get_template('blog/index.html')
#     context = {
#         'posts': posts,
#     }
#     return HttpResponse(template.render(context, request))

# # test stuff


# def detail(request, question_id):
#     post = Post.objects.order_by('created_date')[question_id-1]
#     template = loader.get_template('blog/detail.html')
#     context = {
#         'post': post,
#     }
#     return HttpResponse(template.render(context, request))


# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)


# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        """Return the last five published questions."""
        return Post.objects.order_by('created_date')[:5]


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'


class ResultsView(generic.DetailView):
    model = Post
    template_name = 'blog/results.html'


def edit(request, question_id):
    post = Post.objects.order_by('created_date')[question_id-1]
    template = loader.get_template('blog/edit.html')
    context = {
        'post': post,
    }
    return HttpResponse(template.render(context, request))

    # same as above, no changes needed.
    #question = get_object_or_404(Post, pk=question_id)
    # try:
    #     selected_choice = question.author.get(pk=request.POST['choice'])
    # except (KeyError, Author.DoesNotExist):
    #     # Redisplay the question voting form.
    #     return render(request, 'blog/detail.html', {
    #         'question': question,
    #         'error_message': "You didn't select a choice.",
    #     })
    # else:
    #     selected_choice.votes += 1
    #     selected_choice.save()
    #     # Always return an HttpResponseRedirect after successfully dealing
    #     # with POST data. This prevents data from being posted twice if a
    #     # user hits the Back button.
    # return HttpResponseRedirect(reverse('post:edit', args=(question.id,)))
