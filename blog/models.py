from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# class PublishedManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(publish='publish')


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    body = models.TextField()
    publish = models.DateField(auto_now_add=True)

    # objects = models.Manager()  # the default manager
    # published = PublishedManager()  # custom manager
    
    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=100, default='')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)



