from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from .models import Post
from .forms import CommentForm

# Create your views here.


def blog_home(request):
    object_list = Post.objects.order_by('-publish')

    # #my addition
    # post = get_object_or_404(Post)
    # comments = post.comments.filter(active=True)

    paginator = Paginator(object_list, 3) # 6 posts per page
    page = request.GET.get('page')
    try:
        latest_posts = paginator.page(page)
    except PageNotAnInteger:
        #if page is not an integer deliver the first page
        latest_posts = paginator.page(1)
    except EmptyPage:
        #fi page is out of range, deliver the last page
        latest_posts = paginator.page(paginator.num_pages)

    template = 'exoticgetaways/blog.html'
    context = {'latest_posts': latest_posts, 'page': page}
    # print(latest.id)
    return render(request, template, context)


def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    #list of active comments
    comments = post.comments.filter(active=True)

    if request.method == 'POST':
        #a comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            #create comment object but dont save to database yet
            new_comment = comment_form.save(commit=False)
            #assign the current post to the comment
            new_comment.post = post
            #save the comment to the database
            new_comment.save()
            return redirect('blog:blog_detail', pk=post.pk)

    comment_form = CommentForm()

    template = 'exoticgetaways/details.html'
    context = {'post': post, 'comments': comments, 'comment_form': comment_form}
    return render(request, template, context)



