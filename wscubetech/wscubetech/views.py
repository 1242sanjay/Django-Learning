from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect    # both HttpResponseRedirect and redirect used for redirecting page
from .forms import usersForm
from course.models import Course
from news.models import News
from django.core.paginator import Paginator
from contact.models import Contact
from django.core.mail import send_mail, EmailMultiAlternatives


def homePage(request):

#     send_mail(
#     'Subject here',
#     'Here is the message.',
#     'sraj8948225@gmail.com',
#     ['1242sanjay@gmail.com'],
#     fail_silently=False,
# )

    subject='Testing mail'
    from_email='sraj8948225@gmail.com'
    msg='<p>Welcome to <b>django</b> mail sending</p>'
    to='1242sanjay@gmail.com'
    msg=EmailMultiAlternatives(subject, msg, from_email, [to])
    msg.content_subtype='html'
    msg.send()

    newsData = News.objects.all()
    courseData = Course.objects.all().order_by('-course_name')[:3]
   
    data = {
        'courseData':courseData,
        'newsData':newsData
    }
    return render(request, "index.html", data)

    
def aboutUs(request):
    
    return render(request, "about.html")


def courses(request):
    courseData = Course.objects.all().order_by('course_name')
    paginator = Paginator(courseData, 1)
    page_number=request.GET.get('course_page')
    courseDataFinal = paginator.get_page(page_number)
    totalpage = courseDataFinal.paginator.num_pages
    # print(courseData)
    # for course in courseData:
    #     print(course)
    #     print(course.course_name)


    if request.method == 'GET':
        ct = request.GET.get("coursename")
        if ct != None:
            courseDataFinal = Course.objects.filter(course_name__icontains=ct)

    data = {
        'courseData':courseDataFinal,
        'lastpage' : totalpage,
        'pagelist' : [i+1 for i in range(totalpage)]
    }
    return render(request, "courses.html", data)


def courseDetails(request, courseid):
    return HttpResponse("The course id is {}".format(courseid))


def contact(request):
    return render(request, "contact.html")


def events(request):
    return render(request, "events.html")


def trainer(request):
    return render(request, "trainers.html")

def userForm(request):
    fm = usersForm()
    ans = 0
    data = {'form':fm}
    try:
        # n1 = int(request.GET['num1'])
        # n2 = int(request.GET.get('num2'))
        # print(n1+n2)
        # ans = n1 + n2

        if request.method =="POST":
            n1 = int(request.POST['num1'])
            n2 = int(request.POST.get('num2'))
            ans = n1 + n2
            data = {
                'form':fm,
                'n1': n1,
                'n2': n2,
                'output': ans
            }
            url = "/about-us/?output={}".format(ans)
            return HttpResponseRedirect(url)
    except:
        pass
    return render(request, "userForm.html", data)


def submitForm(request):
    ans = 0
    data = {}
    try:
        # n1 = int(request.GET['num1'])
        # n2 = int(request.GET.get('num2'))
        # print(n1+n2)
        # ans = n1 + n2

        if request.method =="POST":
            n1 = int(request.POST['num1'])
            n2 = int(request.POST.get('num2'))
            ans = n1 + n2
            data = {
                'n1': n1,
                'n2': n2,
                'output': ans
            }
            # url = "/about-us/?output={}".format(ans)
            # return redirect(url)
            return HttpResponse(ans)
    except:
        pass


def calculator(request):
    result = 0
    try:
        if request.method == 'POST':
            error1 = False if request.POST.get('num1') else True
            error2 = False if request.POST.get('num2') else True
            print("error1", error1)
            print("error2", error2)
            if error1 == True or error2 == True:
                return render(request, "calculator.html", {'e_num1':error1, 'e_num2':error2})
              
            else:
                num1 = eval(request.POST.get('num1'))
                num2 = eval(request.POST.get('num2'))
                operator = request.POST.get('operator')
                if operator == '+':
                    result = num1 + num2
                elif operator == '-':
                    result = num1 - num2
                elif operator == '*':
                    result = num1 * num2
                elif operator == '/':
                    result = num1 / num2
    except:
        result = "Invalid Operation"
    print(result)
    return render(request, "calculator.html", {'result':result})


def newsDetails(request, news_slug):
    newsDetail = News.objects.get(news_slug=news_slug)
    return render(request, "newsdetails.html", {'newsDetail': newsDetail})


def contactMessage(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        msg = Contact(contact_name=name, contact_email=email, contact_sub=subject, contact_message=message)
        msg.save()
    return render(request, "contact.html")
