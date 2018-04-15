from django.shortcuts import render
from django.utils import timezone   # +2)
from .models import Post    # +1)
from django.shortcuts import render, get_object_or_404  # +5)

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')  # +3)
#///    return render(request, 'blog/post_list.html', {})
    return render(request, 'blog/post_list.html', {'posts': posts}) # +4)

def post_detail(request, pk):   # +6)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
