from django.shortcuts import render
from .forms import BlogForm

def add_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog_item = form.save(commit=False)
            blog_item.save()
    else:
        form = BlogForm()
    return render(request, 'blog/blog_form.html', {'form' : form})

def display(request):
    show = Blog.objects.all()
    return render(request, 'blog/blog_form.html', {'show' : show})
