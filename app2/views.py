from django.shortcuts import render

# Create your views here.
def third(request):
    dict = {'Exam':'Apptitude', 'Date':'29/12/2022', 'Time':'02:00pm'}
    return render(request, 'three.html',context=dict)

def fourth(request):
    return render(request, 'four.html')