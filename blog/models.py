from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator
# Create your models here.


class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self):
        return self.full_name()
class Tag(models.Model):
    caption=models.CharField(max_length=100)
class Post(models.Model):
    title=models.CharField(max_length=100,null=True)
    author=models.ForeignKey(Author,on_delete=models.SET_NULL,related_name="post",null=True)
    excerpt=models.CharField(max_length=200,null=True)
    image=models.ImageField(upload_to="images",null=True)
    date=models.DateField(auto_now=True)
    slug=models.SlugField(unique=True,default="",null=True)
    content=models.TextField(validators=[MinLengthValidator(10)])
    caption=models.ManyToManyField(Tag)

    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        super().save(*args,**kwargs)
    def __str__(self) -> str:
        return f"{self.title}, {self.author}"
class Comments(models.Model):
    user_name=models.CharField(max_length=100)
    email=models.EmailField()
    comment=models.TextField(max_length=1000)
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments",null=False)
