from django.http import HttpResponse
from django.shortcuts import render


def homePage(request):
    data = {
        'title':'Home Page',
        'bdata':'Welcome to my first django project',
        'clist':['Python', 'Java', 'PHP'],
        'student_details':[
            {'name':'Pradeep', 'phone':9269452813},
            {'name':'Karan', 'phone':9290452813}
        ],
        'numbers':[10, 20, 30, 40, 50, 60, 70, 80]
    }
    return render(request, "index.html", data)

    
def aboutUs(request):
    return HttpResponse("Welcome to my first Django project")


def course(request):
    return HttpResponse("Welcome to our courses")


def courseDetails(request, courseid):
    return HttpResponse("The course id is {}".format(courseid))


