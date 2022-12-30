from django.shortcuts import render

# Create your views here.
def first(request):
    dict = {'Name': 'Kushal', 'Age':'23', 'Course': 'Django',}
    return render(request, 'one.html',context=dict)

def second(request):
    dict = {'Trainer': 'Harshad', 'Course': 'Django','Time':'12:00pm'}
    return render(request, 'two.html',context=dict)