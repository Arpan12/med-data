import json

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import (HttpResponse, HttpResponseBadRequest,
                         HttpResponseForbidden)
from django.shortcuts import get_object_or_404, render
from django.template.context_processors import csrf
from django.template.loader import render_to_string
from django.conf import settings

from .models import Post,Answers
from .forms import PostArea


# Create your views here.
@login_required
def posts(request,username):
    post_list=Post.objects.all()
    page=1
    paginator=None
    page=request.GET.get(page,1)
    paginator=Paginator(post_list,10)
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        posts=paginator.page(page)
    except EmptyPage:
        posts=paginator.page(Paginator.num_pages)       
    
    csrf_token = (csrf(request)['csrf_token'])

    form=request.POST

    if request.method=="POST":
        NewPost=Post()
        NewPost.user=request.user
        NewPost.post=form['new_post']
        NewPost.save()
        return render(request,"forum/posts.html",{"message":"yor question is saved",'user':request.user,'posts':posts,'csrf_token': csrf_token})
    
    return render(request,"forum/posts.html",{'form':form,'user':request.user,'posts':posts,'csrf_token': csrf_token})

def upvoteAnswerToggle(request,username,answer_id):
    
    if request.method == "POST":
        answer=get_object_or_404(Answers,id=answer_id)
        user=request.user
        
        if user in answer.upvotes.all():
            answer.upvotes.remove(user)
        else:
            answer.upvotes.add(user)
        answer.save()
    

    return HttpResponse("")    