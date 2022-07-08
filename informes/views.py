from django.shortcuts import render, redirect
from .forms import  PostForm
from django.contrib.auth.models import User, Group
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required


from .models import Post
# Create your views here.



@login_required
def procurar(request):
    list_filter = Post.objects.order_by('title').filter(postar=True)
    
    if 'procurar' in request.GET:
        nome = request.GET['procurar']
        if nome:
            list_filter = list_filter.filter(title__icontains=nome)

    return render(request, 'informes/procurar.html', {'posts': list_filter})

@login_required
def procure(request):
    list_filter = Post.objects.order_by('created_at').filter(postar=True)
    
    if 'procure' in request.GET:
        nome = request.GET['procure']
        if nome:
            list_filter = list_filter.filter(created_at__year=nome)

    return render(request, 'informes/procurar.html', {'posts': list_filter})

@login_required
def dia(request):
    list_filter = Post.objects.order_by('created_at').filter(postar=True)
    
    if 'dia' in request.GET:
        nome = request.GET['dia']
        if nome:
            list_filter = list_filter.filter(created_at__day=nome)

    return render(request, 'informes/procurar.html', {'posts': list_filter})

@login_required
def hora(request):
    list_filter = Post.objects.order_by('created_at').filter(postar=True)
    
    if 'hora' in request.GET:
        nome = request.GET['hora']
        if nome:
            list_filter = list_filter.filter(created_at__hour=nome)

    return render(request, 'informes/procurar.html', {'posts': list_filter})



@login_required
def post(request):
    posts = Post.objects.all()

    if request.method == "POST":
        post_id = request.POST.get("post-id")
        user_id = request.POST.get("user-id")

        if post_id:
            post = Post.objects.filter(id=post_id).first()
            if post and (post.author == request.user or request.user.has_perm("main.delete_post")):
                post.delete()
        elif user_id:
            user = User.objects.filter(id=user_id).first()
            if user and request.user.is_staff:
                try:
                    group = Group.objects.get(name='default')
                    group.user_set.remove(user)
                except:
                    pass

                try:
                    group = Group.objects.get(name='mod')
                    group.user_set.remove(user)
                except:
                    pass
    
    return render(request, 'informes/post.html', {"posts": posts})




@permission_required('informes.post')
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("/informes/post/")
    else:
        form = PostForm()

    return render(request, 'informes/create_post.html', {"form": form})
