from django.db import models

# Create your models here.
from django.contrib.auth.models import User

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=100,unique=True,null=False)
    slug = models.SlugField(max_length=100,unique=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_post')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS,default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


