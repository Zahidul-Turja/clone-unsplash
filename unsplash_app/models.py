from django.db import models

# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class User(models.Model):
    name = models.CharField(max_length=50)
    user_name = models.CharField(primary_key=True, max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    profile_image = models.ImageField(null=True)

    def __str__(self):
        return f"{self.user_name} {self.email}"


class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    author = models.ForeignKey(User,
                               on_delete=models.SET_NULL,
                               null=True,
                               related_name="posts")
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title} {self.author}"
