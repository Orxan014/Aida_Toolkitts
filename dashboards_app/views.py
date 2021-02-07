from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.http import HttpResponse, JsonResponse
from .forms import PostForm
from .models import Calendar


def calendar(request):

    return render(request, 'calendar.html')


# Create your views here.

def add_post(request):
    if request.method == 'POST':

        if request.is_ajax():
            print("AJAX")

            content = request.POST.get("content")
            postid = request.POST.get("postid")
            post_image = request.POST.get("post_image")
            print(post_image)

            if postid == 'nonee':

                if content != '':
                    test = Calendar.objects.create(post=content,post_image=post_image)
                    id = test.id
                    return JsonResponse({
                        'id': id
                    })
            else:
                test = Calendar.objects.filter(id=int(postid)).last()
                test.post = content
                test.post_image = post_image
                test.save()
                return JsonResponse({
                    'status': 'oke'
                })
        else:
            print("Error not AJAX request")
    return render(request, 'post_add.html')
