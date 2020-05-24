from django.views import generic
from django.shortcuts import render
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def blog_detail(request, slug):
    post = Post.objects.get(slug=slug)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
    }

    return render(request, "post_detail.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)

    # def upload_file(request):
    #     if request.method == 'POST':
    #         form = UploadFileForm(request.POST, request.FILES)
    #         if form.is_valid():
    #             handle_uploaded_file(request.FILES['file'])
    #             return HttpResponseRedirect('/success/url/')
    #     else:
    #         form = UploadFileForm()
    #     return render(request, 'upload.html', {'form': form})

    