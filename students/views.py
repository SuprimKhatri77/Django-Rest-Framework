from django.shortcuts import render,HttpResponse

# Create your views here.
def students(request):
    students = [
        {
            'id':1,
            'name':'john doe',
            'age':22
        }
    ]
    return HttpResponse(students)