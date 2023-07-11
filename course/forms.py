from django import forms
from course.models import Catogaries, Course

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Catogaries
        fields = ['name', 'category_image']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['featured_image', 'video_file', 'title', 'category', 'description', 'status']
