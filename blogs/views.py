from django.shortcuts import render, redirect
from django.views.generic import ListView
from hitcount.views import HitCountDetailView

from .forms import CommentForm, ContactForm
from .models import Posts, Comment


# CBV

class PostListView(ListView):
    queryset = Posts.objects.all()[:6]
    template_name = 'blogs/index.html'
    context_object_name = 'posts'
    paginate_by = 6


class PostDetailView(HitCountDetailView):
    model = Posts
    template_name = 'blogs/single-standard.html'
    context_object_name = 'posts'
    pk_url_kwarg = 'pk'
    form = CommentForm

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()

        return redirect('/')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_post'] = Posts.objects.all()[:6]
        context['comments'] = Comment.objects.filter(post_id=self.kwargs['pk'])
        context['form'] = self.form
        return context


# FBC

def about(request):
    context = {
        'all_post': Posts.objects.all()[:6],
    }

    return render(request, 'blogs/about.html', context)


def contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        print(form.data)

    context = {
        'form': form,
        'all_post': Posts.objects.all()[:6],
    }

    return render(request, 'blogs/contact.html', context)
