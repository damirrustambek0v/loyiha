from django.shortcuts import render, redirect

from .models import Post

def post_list(request):
    posts = Post.objects.all()
    ctx = {'posts': posts}
    return render(request, 'programs/program-form.html', ctx)


def post_create(request):
    title = request.POST.get('title')
    description  = request.POST.get('description ')
    if title and description :
        Post.objects.create(
            title=title,
            description=description
        )
        return redirect('programs:post_list')
    return render(request, 'programs/program-list.html')





