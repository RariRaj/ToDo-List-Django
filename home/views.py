from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from home.models import Task
from home.forms import ListForm
from django.contrib import messages

# Create your views here.
def index(request):
    context={'success':False}
    if request.method=="POST":
        title=request.POST['title']
        description=request.POST['description']
        

        inst=Task(taskTitle=title,taskDesc=description)
        inst.save()
        context={'success':True}
    return render(request,'index.html',context)

    
      

        
    

def task(request):

    allTasks=Task.objects.all()
    # print(allTasks)
    # for item in allTasks:
    #     print(item.taskTitle)
    context={'tasks':allTasks}
    return render(request,'tasks.html',context)


def delete(request,id):
    item=Task.objects.get(pk=id)
    item.delete()
    messages.success(request,('Item has been deleted from List'))
    return redirect('task')

def cross_off(request,id):
    item=Task.objects.get(pk=id)
    item.taskCompleted=True
    item.save()
    return redirect('task')

def uncross(request,id):
    item=Task.objects.get(pk=id)
    item.taskCompleted=False
    item.save()
    return redirect('task')

def update(request,id):

    item=Task.objects.get(pk=id)
    
    form = ListForm(instance = item)

    if request.method=="POST":
        form=ListForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request,('Item has been edited')) 
            return redirect('task')

    context={'form':form} 
      
    return render(request,'update_item.html',context)
            
            
             
    

def test(request):
    return render(request,'test.html')