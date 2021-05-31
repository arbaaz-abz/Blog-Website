from django.shortcuts import render , get_object_or_404
from . import models

# Create your views here.
def blog(request):
	#Make a list which contains all objects of type Post , ordered by date
	posts = models.Post.objects.order_by('-pub_date')
	return render(request,'blogposts/index.html',{'posts':posts})

def about(request):
	return render(request,'about/about.html')

def post_extend(request,p_id):
	post_obj = get_object_or_404(models.Post , pk=p_id)
	return render(request,'blogposts/post_detail.html',{'post' : post_obj})
