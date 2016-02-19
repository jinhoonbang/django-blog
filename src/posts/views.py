from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm
from .models import Post

# Create your views here.

def post_create(request):
    #allows validation, "This field is required"
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Succesfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Not Successfully Created")

    # if request.method == "POST":
    #     print(request.POST.get("content"))
    #     title = request.POST.get("title")
        #does not provide validation
        #Post.objects.create(title=title)
    context = {
        "form": form,
    }
    return render(request, "post_form.html", context)

def post_detail(request, id=None):

    instance = get_object_or_404(Post, id = id)

    context = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request, "post_detail.html", context)

def post_list(request):

    queryset = Post.objects.all()

    context = {
        "objects_list" : queryset,
        "title": "List",
    }

    #return HttpResponse("<h1>List</h1>")
    return render(request, "post_list.html", context)

def post_update(request, id=None):
    instance = get_object_or_404(Post, id = id)
    form = PostForm(request.POST or None, instance = instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "<a href='#'>Item Saved</a>", extra_tags = 'html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request, "post_form.html", context)


def post_delete(request, id=None):
    instance = get_object_or_404(Post, id = id)
    instance.delete
    messages.success(request, "Succesfully Deleted")
    return redirect("list")

