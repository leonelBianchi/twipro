from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy, reverse

# Create your views here.

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get("post_id"))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse("article-detail", args=[str(pk)]))

def index(request, id):
    ls = ToDoList.objects.get(id=id) # obtengo el nombre del id = id (el ignresado en la url en urls.py del main)
    
    if request.method == "POST":
        print(request.POST)
        if request.POST.get("save"):
            for item in ls.item_set.all():
                if request.POST.get("c" + str(item.id)) == "clicked":
                    item.complete=True
                else:
                    item.complete=False
                
                item.save()
        elif request.POST.get("newItem"):
            txt = request.POST.get("new")
            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("invalid")
            

    
    return render(request, "main/list.html", {"ls":ls})

def home(request):
    return render(request, "main/home.html", {})
    
def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            response.user.ToDoList.add(t)

        return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateNewList()

    return render(response, "main/create.html", {"form":form})

#def view(response):
#    return render(response, "main/view.html", {})

class HomeView(ListView):
    model = Post
    template_name = "main/view.html"
    ordering = ["-post_date"]

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = "main/articles_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs["pk"])
        total_likes = stuff.total_likes()
        context["total_likes"] = total_likes
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "main/add_post.html"
    #fields = "__all__"

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "main/add_comment.html"
    #fields = "__all__"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.post_id = self.kwargs["pk"]
        return super().form_valid(form)

class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "main/update_post.html"
    #fields = "__all__"

class DeletePostView(DeleteView):
    model = Post
    template_name = "main/delete_post.html"
    success_url = reverse_lazy("view")