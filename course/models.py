from django.db import models

class Catogaries(models.Model):
    icon = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    category_image = models.ImageField(upload_to="Media/course", blank=True)

    def __str__(self):
        return(self.name)

class Author(models.Model):
    author_profile = models.ImageField(upload_to="Media/author",blank=True)
    name = models.CharField(max_length=100, null=True)
    about_author = models.TextField()

    def __str__(self):
        return self.name


class Course(models.Model):
    STATUS = (
        ('PUBLISH','PUBLISH'),
        ('DRAFT', 'DRAFT'),
    )

    featured_image = models.ImageField(upload_to="Media/featured_img",blank=True)
    # featured_video = models.CharField(max_length=300,null=True)
    video_file = models.FileField(upload_to='videos/', null=True)
    title = models.CharField(max_length=500)
    created_at = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,null=True)
    category = models.ForeignKey(Catogaries,on_delete=models.DO_NOTHING)
    description = models.TextField()
    price = models.IntegerField(null=True,default=0)
    discount = models.IntegerField(null=True)
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)
    status = models.CharField(choices=STATUS,max_length=100,null=True)


    def __str__(self):
        return self.title

