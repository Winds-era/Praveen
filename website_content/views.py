from django.shortcuts import render, redirect
from course.models import Catogaries, Course
from course.forms import CategoryForm, CourseForm

# Create your views here.
def home_view(request):
    catogery = Catogaries.objects.all()
    course = Course.objects.filter(status='PUBLISH').order_by('-id')
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = CategoryForm()
    context = {
        'catogery': catogery,
        'course': course,
        'form': form
    }
    if not request.user.is_authenticated:
        return redirect('user_account:login_first')
    return render(request, 'website_content/home_page.html', context)


def course_detail(request, name):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = CourseForm()
    filtered_courses = Course.objects.filter(category=Catogaries.objects.get(name=name))
    context = {
        'filtered_courses': filtered_courses,
        'form': form
    }
    if request.user.user_role == 'STUDENT':
        return render(request, 'courses/filtered_course.html', context)
    else:
        return render(request, 'courses/M_filtered.html', context)


def filtered_content(request, name, slug):
    courses = Course.objects.filter(slug=slug)

    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=courses.first())  # Pass the instance to the form for updating
        if form.is_valid():
            form.save()
    else:
        form = CourseForm(instance=courses.first())  # Pass the instance to the form for pre-populating fields

    context = {
        'courses': courses,
        'form': form,
        'slug': slug,
    }

    if request.user.user_role == 'STUDENT':
        return render(request, 'courses/course_content.html', context)
    else:
        return render(request, 'courses/M_course.html', context)
    

#membership pages
def plan_details(request):
    return render(request, 'website_content/plans.html')
