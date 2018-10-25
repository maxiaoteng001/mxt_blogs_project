from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    # 文章标题
    title = models.CharField(max_length=70)
    
    # 文章正文 textField存储更多的内容
    body = models.TextField()

    # 创建时间和最新修改时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    # 文章摘要, 指定blank=True可以为空
    excerpt = models.CharField(max_length=200, blank=True)

    # 标签和分类, 标签可以为空, 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    # User表是django自带的,
    # django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是 Django 为我们已经写好的用户模型。
    # 一个文章只有一个作者, 一个作者有多篇文章, 所以是一对多
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
