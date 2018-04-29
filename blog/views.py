from django.shortcuts import redirect	# +8) Добавь эту строку в начало файла
from django.shortcuts import render
from django.utils import timezone   # +2)
from .models import Post    # +1)
from django.shortcuts import render, get_object_or_404  # +5)
from .forms import PostForm # +7)

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')  # +3)
#///    return render(request, 'blog/post_list.html', {})
    return render(request, 'blog/post_list.html', {'posts': posts}) # +4)

def post_detail(request, pk):   # +6)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

#  +8)
# def post_new(request):
#    form = PostForm()
#    return render(request, 'blog/post_edit.html', {'form': form})

#   +9)
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

#   +10)
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
