from django.shortcuts import render, redirect
from course.models import Catogaries, Course


# Create your views here.
def home_view(request):
    catogery = Catogaries.objects.all()
    course = Course.objects.filter(status='PUBLISH').order_by('-id')
    context = {
        'catogery': catogery,
        'course': course,
    }
    if not request.user.is_authenticated:
        return redirect('user_account:login_first')
    return render(request, 'website_content/home_page.html', context)


def course_detail(request, name):
    context = {}
    context['filtered_courses'] = Course.objects.filter(
        category=Catogaries.objects.get(name=name))
    return render(request, 'courses/filtered_course.html', context)


def filtered_content(request, name, slug):
    a = Course.objects.filter(slug=slug)
    context = {
        'a': a
    }
    return render(request, 'courses/course_content.html', context)
