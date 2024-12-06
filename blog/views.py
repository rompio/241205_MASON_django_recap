from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    # Query all Post objects from the database
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    
    # Render the posts using the 'post_list.html' template
    return render(request, 'post_list.html', context=context)

def post_detail(request, pk):
    # Retrieve the post with the given pk (primary key) or return a 404 if not found
    post = get_object_or_404(Post, pk=pk)

    # Create a context to pass to the template
    context = {
        'post': post
    }

    # Render the 'post_detail.html' template and pass the context
    return render(request, 'blog/post_detail.html', context)