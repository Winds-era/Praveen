from django.db import models


class Catogaries(models.Model):
    name = models.CharField(max_length=200, null=True)
    category_image = models.ImageField(upload_to="course/", blank=True)

    def __str__(self):
        return(self.name)


class Course(models.Model):
    STATUS = (
        ('PUBLISH', 'PUBLISH'),
        ('DRAFT', 'DRAFT'),
    )

    featured_image = models.ImageField(upload_to="featured_img/", blank=True)
    video_file = models.FileField(upload_to='videos/', null=True)
    title = models.CharField(max_length=500)
    created_at = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Catogaries, on_delete=models.DO_NOTHING)
    description = models.TextField()
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)
    status = models.CharField(choices=STATUS, max_length=100, null=True)

    def __str__(self):
        return self.title
    
