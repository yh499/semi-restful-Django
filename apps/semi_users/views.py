from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from .models import user


def index(request):
    context = {
        'user': user.objects.all()
    }
    return render(request, 'semi_users/index.html', context)

    
def new(request):
    return render(request, 'semi_users/new.html')


def create(request):
    if request.method =="POST":
        user.objects.create(firstname = request.POST['firstname'], lastname = request.POST['lastname'], email = request.POST['email'])

    return redirect('/')

def users(request):
    return render(request, 'semi_users/index.html')


def show(request, user_id):
    print user_id
    userobj = user.objects.get(id=user_id)
    print userobj
    return render(request, 'semi_users/show.html', {'user':userobj}) 


def delete(request, user_id):
    user.objects.get(id=user_id).delete()
    return redirect('/')


def update(request, user_id):
    print user_id
    if request.method == 'POST':
        updated_info = user.objects.get(id=user_id)
        updated_info.firstname = request.POST['firstname']
        updated_info.lastname = request.POST['lastname']            
        updated_info.email = request.POST['email']
        updated_info.save()
        
    return redirect('/')



def edit(request, user_id):
    
    return render(request, 'semi_users/edit.html', {'user':user.objects.get(id=user_id)}) 