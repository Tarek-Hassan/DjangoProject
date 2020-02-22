from django.shortcuts import render
from django.views import generic
from blog.models import Post, Reply, Comment
from .forms import CommentForm, ReplyForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request,'blogviews/home.html')

def post_list(request):
    template_name = 'blogviews/allPosts.html'
    posts = Post.objects.all()

    context = {'post_list': posts}

    return render(request, template_name, context)

def post_detail(request, slug):
    template_name = 'blogviews/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    replies = Reply.objects.all()
    reply_form = ReplyForm()
    new_comment = None

    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            new_comment.name = request.user
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,
                                           'replies': replies,
                                           'reply_form': reply_form})

# @login_required
def comment_reply(request, commentId, slug):
    comment = get_object_or_404(Comment, id=commentId)
    print(comment)
    url = '/blog/'+ slug

    if request.method == 'POST':
        print (request.GET)
        reply_form = ReplyForm(data=request.POST)
        print (reply_form)
        if reply_form.is_valid():

            # Create Comment object but don't save to database yet
            reply = reply_form.save(commit=False)
            # Assign the current post to the comment
            reply.comment = comment
            reply.name = request.user
            # Save the comment to the database
            reply.save()
    else:
        reply_form = ReplyForm()

    return HttpResponseRedirect(url)